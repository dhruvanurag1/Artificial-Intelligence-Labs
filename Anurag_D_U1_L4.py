# Name: Dhruv Anurag         Date: 9/29/21
import random, time, math

class HeapPriorityQueue():
   # copy your HeapPriorityQueue() from Lab3
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      # write more code here to keep the min-heap property
      if len(self.queue) > 3:
         self.heapUp(len(self.queue) - 1)
      elif len(self.queue) == 3 and self.queue[1] > self.queue[2]:
         self.swap(1,2)

   # helper method for push      
   def heapUp(self, k):
      a = k//2
      if a < 1:
         return
      else:
         if self.queue[k] > self.queue[a]:
            return
         else:
            self.swap(k, a)
            self.heapUp(a)
               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      left, right = k * 2, (k * 2) + 1
      if(k >= size or (left >= size and right >= size)):
         return
      else:
         if right < size:
            min = 0
            if self.queue[left] < self.queue[right]:
               min = left
            else:
               min = right
            if self.queue[k] > self.queue[min]:
               self.swap(k, min)
               self.heapDown(min, size)

   # make the queue as a min-heap            
   def reheap(self):
      for i in range(len(self.queue)-1, 1, -1):
         self.swap(1, i)
         self.heapDown(1, i-1)
      self.queue.insert(1, self.queue[-1])
      self.queue = self.queue[:-1]
      return self.queue
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
     # Your code goes here
      a = self.queue[1]
      if len(self.queue) <= 1:
         return
      elif len(self.queue) < 3:
         self.queue.pop(1)
      elif len(self.queue) == 3 and self.queue[1] > self.queue[2]:
         self.swap(1, 2)
         self.queue.pop(1)
      else:
         self.swap(1, len(self.queue) - 1)
         self.queue.pop(len(self.queue) - 1)
         self.heapDown(1, len(self.queue))
      return a
      # change this
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      # Your code goes here
      index += 1
      r = self.queue[index]
      self.queue[index] = self.queue[-1]
      self.queue = self.queue[:-1]
      parent = index // 2
      if parent == 1 or self.queue[parent] < self.queue[index]:
         self.heapDown(index, len(self.queue))
      else :
         self.heapUp(index)
      return r


def inversion_count(new_state, width = 4, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   return [[(inv_count := sum(sum(new_state[i] > new_state[j] for j in range(i+1, len(new_state))) for i in range(len(new_state)))) % 2 == 1, inv_count % 2 == 0][new_state.index('_')//N % 2 == 0], inv_count % 2 == 0][N % 2 == 1]

   # Your code goes here

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)


def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
def swap(n, i, j):
   # Your code goes here
   a = list(n)
   a[i], a[j] = a[j], a[i]
   return ''.join(a)
      
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state, size=4):
   children = []
   blank = state.find('_')
   '''your code goes here'''
   if state.index("_") >= size:
      children.append(swap(state, state.index("_"), state.index("_")-size))
   if state.index("_") < size * size - size: 
      children.append(swap(state, state.index("_"), state.index("_")+size))
   if state.index("_") % size != size - 1:
      children.append(swap(state, state.index("_"), state.index("_")+1))
   if state.index("_") % size != 0:
      children.append(swap(state, state.index("_"), state.index("_")-1))
   return children

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   # Your code goes here
   return sum(abs((i//size)-((index := goal.find(state[i]))//size))+abs((i%4) - (index % 4)) for i in range(len(goal)))
   
def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b) 

def a_star(start, goal="1523496_87ABCDEF", heuristic=dist_heuristic, size = 4):
   frontier = HeapPriorityQueue()
   explored = {start : 0}
   path = {start : "s"}
   if start == goal: return []
   else:
      cost = dist_heuristic(start)
      frontier.push((cost, start))
      while frontier.isEmpty() == False:
         a = frontier.pop()
         if a[1] == goal:
            return getPath(a[1], path)
         for i in generate_children(a[1]):
            costs = explored[a[1]] + 1
            if i not in explored or costs < explored[i]:
               explored[i] = costs
               cost2 = dist_heuristic(i)
               b = explored[i] + cost2
               path[i] = a[1]
               frontier.push((b, i))
   return None

def getPath(a, explored):
   path = [a]
   while explored[a] != "s": #"s" is initial's parent
      path.append(explored[a])
      a = explored[a]
   return path[::-1]

   # Your code goes here

def main():
    # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   initial_state = getInitialState("_123456789ABCDEF", 4)
   initial_state = input("Type initial state: ")
   if inversion_count(initial_state):
      cur_time = time.time()
      path = (a_star(initial_state))
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()


''' Sample output 1

Inversion works?: True
Heuristic works?: True
Type initial state: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0


Sample output 2

Inversion works?: True
Heuristic works?: True
Type initial state: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005014657974243164


Sample output 3

Inversion works?: True
Heuristic works?: True
Type initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.27825474739074707


Sample output 4

Inversion works?: True
Heuristic works?: True
Type initial state: 8293AC4671FEDB5_
8293    8293    8293    8293    8293    8293    8293    8293    82_3    8_23    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
AC46    AC46    AC46    AC46    AC46    _C46    C_46    C4_6    C496    C496    C_96    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
71FE    71F_    71_F    7_1F    _71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5_    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 39
Duration:  0.7709157466888428

'''