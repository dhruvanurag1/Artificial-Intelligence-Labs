import random

def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return "12345678_"
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j):
   '''your code goes here'''
   state = list(state)
   state[i], state[j] = state[j], state[i]
   return ''.join(state)
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
   a = []
   if state.index("_") >= 3:
    a.append(swap(state, state.index("_"), state.index("_")-3))
   if state.index("_") < 6: 
    a.append(swap(state, state.index("_"), state.index("_")+3))
   if state.index("_") % 3 != 2:
    a.append(swap(state, state.index("_"), state.index("_")+1))
   if state.index("_") % 3 != 0:
    a.append(swap(state, state.index("_"), state.index("_")-1))
   return a
   
def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   print ("\n\nThe shortest path length is :", len(l))
   return ""

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state):

   explored = {initial_state:"s"}
   q = []
   q.append(initial_state)
   while len(q) > 0:
       if len(q) == 0:
        return ("No solution")
       s = q.pop(0)
       if s == "_12345678":
           return display_path(s, explored)
       for a in generate_children(s):
           if a not in explored:
             q.append(a)
             explored[a] = s
   '''Your code goes here'''

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial):
   explored = {initial:"s"}
   q = []
   q.append(initial)
   while len(q) > 0:
       if len(q) == 0:
        return ("No solution")
       s = q.pop()
       if s == "_12345678":
           return display_path(s, explored)
       for a in generate_children(s):
           if a not in explored:
             q.append(a)
             explored[a] = s
   '''Your code goes here'''
   return ("No solution")


def main():
   initial = "5246317_8"
   print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (BFS(initial))
   print ("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (DFS(initial))

if __name__ == '__main__':
   main()