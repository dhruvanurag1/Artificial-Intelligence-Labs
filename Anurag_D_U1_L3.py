# Name: Dhruv Anurag
# Date: 9/26/21

import random

class HeapPriorityQueue():
   
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


# This method is for testing. Do not change it.
def isHeap(heap, k):
   left, right = 2*k, 2*k+1
   if left == len(heap): return True
   elif len(heap) == right and heap[k] > heap[left]: return False
   elif right < len(heap): 
      if (heap[k] > heap[left] or heap[k] > heap[right]): return False
      else: return isHeap(heap, left) and isHeap(heap, right)
   return True
    
# This method is for testing. Do not change it.
def main():
        
   pq = HeapPriorityQueue()    # create a HeapPriorityQueue object
   
   print ("Check if dummy 0 is still dummy:", pq.queue[0])
   
   # assign random integers into the pq
   for i in range(20):
      t = random.randint(10, 99)
      print (t, end=" ")
      pq.push(t)
   
   print ()
   
   # print the pq which is a min-heap
   for x in pq:
      print (x, end=" ")
   print()
   
   # remove test
   print ("Index 4 is removed:", pq.remove(4))
   
   # check if pq is a min-heap
   for x in pq:
      print (x, end=" ")
   print("\nIs a min-heap?", isHeap(pq.queue, 1))
   
   temp = []
   while not pq.isEmpty():
      temp.append(pq.pop())
      print (temp[-1], end=" ")
   
   print ("\nIn ascending order?", temp == sorted(temp))

if __name__ == '__main__':
   main()