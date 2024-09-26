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
   if state.index("_") >= size: children.append(swap(state, state.index("_"), state.index("_")-size))
   if state.index("_") < size * size - size: children.append(swap(state, state.index("_"), state.index("_")+size))
   if state.index("_") % size != size - 1: children.append(swap(state, state.index("_"), state.index("_")+1))
   if state.index("_") % size != 0: children.append(swap(state, state.index("_"), state.index("_")-1))
   return children

def display_path(path_list, size):
   print(path_list)
   print(len(path_list))
   # for n in range(size):
   #    for path in path_list:
   #       print (path[n*size:(n+1)*size], end = " "*size)
   #    print ()
   # print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   # Your code goes here
   return sum(abs((i//size)-((index := goal.find(state[i]))//size))+abs((i%4) - (index % 4)) for i in range(len(goal)))
   
def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b) 
def bucketing(start, goal = "_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   level = 0
   explored = {start : "s"}
   
   bucket = {level:explored}

   return start
def solve(start, goal = "_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   exploredBFS = {goal : "s"}
   count = 0
   count2 = 0
   q = [goal]
   while len(q) > 0 and count < 5:
       s = q[0]
       q = q[1:]
       count += 1
       for a in generate_children(s):
           if a not in exploredBFS:
             q.append(a)
             exploredBFS[a] = s
   print(exploredBFS)
   return []
   explored1 = set()
   explored2 = set()
   # frontier = HeapPriorityQueue()
   # explored = {start : 0}
   # path = {start : "s"}
   # z = HeapPriorityQueue()
   # if start == goal: return []
   # else:
   #    cost = dist_heuristic(start)
   #    frontier.push((cost, start))
   #    while frontier.isEmpty() == False:
   #       a = frontier.pop()
   #       if a[1] in exploredBFS:
   #          # display_path(getPath(a[1], path)[1:], 4)
   #          # print("\n\n")
   #          # display_path(getPath(a[1], exploredBFS)[::-1], 4)
   #          b = getPath(a[1], path)[1:] + getPath(a[1], exploredBFS)[::-1]
   #          z.push((len(b), b))
   #          count2 += 1
   #          if count2 >= 15:
   #             c = z.pop()[1]
   #             return c
   #             #return getPath(a[1], path)[1:] + getPath(a[1], exploredBFS)[::-1]
   #       for i in generate_children(a[1]):
   #          costs = explored[a[1]] + 1
   #          if i not in explored or costs < explored[i]:
   #             explored[i] = costs
   #             cost2 = dist_heuristic(i)
   #             b = explored[i] + cost2
   #             path[i] = a[1]
   #             frontier.push((b, i))
   # return None

   #  frontier = [HeapPriorityQueue(), [goal]]
   #  explored = [{start : 0}, {goal : 0}]
   #  path = [{start : "s"} , {goal : "s"}]
   #  count = 0
   #  if start == goal: return []
   #  else:
   #      cost = dist_heuristic(start)
   #      frontier[0].push((cost, start))
   #      while frontier[0].isEmpty() == False and len(frontier[1]) > 0:
   #          a = ["","_123456789ABCDEF"]
   #          a[0] = frontier[0].pop()
   #          if count < 5:
   #             a[1] = frontier[1].pop(0)
   #          print(a)
   #          print(count)
   #          print(frontier)
   #          #print(a)
   #          # print(explored)
   #          # print(path)
   #          # print(a)
   #          if a[0][1] in explored[1]:
   #             return getPath(a[0][1], path[0]) + getPath(a[0][1], path[1])[:-1]
   #          elif a[1] in explored[0]:
   #             return getPath(a[1], path[0]) + getPath(a[1], path[1])[::-1][1:]
   #          count += 1
   #          for child1, child2 in ((x, y) for x in generate_children(a[0][1]) for y in generate_children(a[1])):
   #              costs = explored[0][a[0][1]] + 1
   #              if child1 not in explored[0] or costs < explored[0][child1]:
   #                explored[0][child1] = costs
   #                cost2 = dist_heuristic(child1)
   #                b = explored[0][child1] + cost2
   #                path[0][child1] = a[0][1]
   #                frontier[0].push((b, child1))
   #              if child2 not in explored[1] and count < 5:
   #                path[1][child2] = a[1]
   #                frontier[1].append(child2)
   #  return start

 
   #  frontier = [HeapPriorityQueue(), HeapPriorityQueue()]
   #  explored = [{start : 0}, {goal : 0}]
   #  path = [{start : "s"} , {goal : "s"}]
   #  if start == goal: return []
   #  else:
   #      cost = [dist_heuristic(start), dist_heuristic(goal, start)]
   #      frontier[0].push((cost[0], start))
   #      frontier[1].push((cost[1], goal))
   #      while frontier[0].isEmpty() == False and frontier[1].isEmpty() == False:
   #          a = [frontier[0].pop(), frontier[1].pop()]
   #          #print(a)
   #          if a[0][1] in explored[1]:
   #             return getPath(a[0][1], path[0]) + getPath(a[0][1], path[1])[:-1]
   #          elif a[1][1] in explored[0]:
   #              return getPath(a[1][1], path[0]) + getPath(a[1][1], path[1])[::-1][1:]
   #          for child1, child2 in ((x, y) for x in generate_children(a[0][1]) for y in generate_children(a[1][1])):
   #              costs = [explored[0][a[0][1]] + 1, explored[1][a[1][1]] + 1]
   #              if child1 not in explored[0] or costs[0] < explored[0][child1]:
   #                explored[0][child1] = costs[0]
   #                cost2 = dist_heuristic(child1)
   #                b = explored[0][child1] + cost2
   #                path[0][child1] = a[0][1]
   #                frontier[0].push((b, child1))
   #              if child2 not in explored[1] or costs[1] < explored[1][child2]:
   #                explored[1][child2] = costs[1]
   #                cost3 = dist_heuristic(child2)
   #                c = explored[1][child2] + cost3
   #                path[1][child2] = a[1][1]
   #                frontier[1].push((c, child2))
   #  return start
def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
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
  # print(explored)
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
      path = (solve(initial_state))
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