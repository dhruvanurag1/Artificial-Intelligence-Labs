# Name: Dhruv Anurag
# Period: 5

from tkinter import *
from graphics import *
import random

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
   ''' your code goes here '''
   return len(vars) == len(assignment)

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   ''' your code goes here '''
   return random.choice([l for l in vars.keys() if l not in assignment])

   
def isValid(value, var, assignment, variables, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   ''' your code goes here '''
   if var not in adjs:
      return True
   adjacents = adjs[var]
   for a in adjacents:
      if a in assignment.keys():
         if value == assignment[a]:
            return False
   return True

def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, variables, adjs, shapes, frame):
   # Refer the pseudo code given in class.
   ''' your code goes here '''
   if check_complete(assignment, variables, adjs): return assignment
   var = select_unassigned_var(assignment, variables, adjs)
   for color in variables[var]:
      if isValid(color, var, assignment, variables, adjs):
         assignment[var] = color
         draw_shape(shapes[var], frame, color)
         r = recursive_backtracking(assignment, variables, adjs, shapes, frame)
         if r != None:
            return r
   #for value in variables
   return None

# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(9999999)] # give some pause
   
def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   ''' your code goes here '''
   with open("/Users/dhruvanurag/Documents/TJ/AI/mcNodes.txt", "r") as file1:
      for line in file1:
         regions.append(line.strip())
   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = {'red', 'green', 'blue'}

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   ''' your code goes here '''
   with open("/Users/dhruvanurag/Documents/TJ/AI/mcEdges.txt", "r") as file2:
      for line in file2:
         line_array = line.strip().split(" ")
         if line_array[0] not in adjacents:
            adjacents[line_array[0]] = {line_array[1]}
         else:
            adjacents[line_array[0]].add(line_array[1])
         if line_array[1] not in adjacents:
            adjacents[line_array[1]] = {line_array[0]}
         else:
            adjacents[line_array[1]].add(line_array[0])
   # Set graphics -- no additional code for this part
   frame = GraphWin('Map', 300, 300)
   frame.setCoords(0, 0, 299, 299)
   shapes = read_shape("/Users/dhruvanurag/Documents/TJ/AI/mcPoints.txt")
   for s, points in shapes.items():
      draw_shape(points, frame, 'white')
  
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
   solution = backtracking_search(variables, adjacents, shapes, frame)
   print (solution)
   
   mainloop()

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''