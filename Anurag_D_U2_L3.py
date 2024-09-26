# Name: Dhruv Anurag
# Date: 11/15/21
import random
import time

def check_complete(assignment, csp_table):
   # temp, complete = [], {'1', '2', '3', '4', '5', '6', '7', '8','9'}
   # for a in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
   #        temp.append({assignment[a], assignment[a+1], assignment[a+2], assignment[a+9], assignment[a+10], assignment[a+11], assignment[a+18]
   #        , assignment[a+19], assignment[a+20]})
   # for a in temp:
   #    if len(a - complete) != 0:
   #       return False
   return assignment.find('.') == -1
   
def select_unassigned_var(assignment, variables, csp_table):
   if assignment.find('.') == -1: return -1
   return min({(len(variables[a]), a) for a in variables})[1]

def isValid(value, var_index, assignment, variables, csp_table):
   for a in csp_table:
      if var_index in a:
             for b in a:
                  if assignment[b] == value: return False
   for vals in variables.values():
      if len(vals) == 0: return False
   return True

def ordered_domain(var_index, assignment, variables, csp_table):
   return []

def update_variables(value, var_index, assignment, variables, csp_table):
   neighbors = {a : {b for c in csp_table if a in c for b in c} for a in range(81)}
   return {a : {'1','2','3','4','5','6','7','8','9'} - {assignment[b] for b in neighbors[a]} for a in range(81) if assignment[a] == '.'}

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   if check_complete(assignment, csp_table): return assignment
   var = select_unassigned_var(assignment, variables, csp_table)
   for a in variables[var]:
      if isValid(a, var, assignment, variables, csp_table):
         assignment = assignment[:var] + a + assignment[var+1:]
         tempvariables = update_variables(a, var, assignment, variables, csp_table)
         r = recursive_backtracking(assignment, tempvariables, csp_table)
         if r != None:
            return r
   return None

def display(solution):
   ans = ""
   for a in range(81):
      ans += solution[a] + " "
      if(a % 3 == 2): ans += " "
      if(a % 9 == 8): ans += "\n"
      if a == 26 or a == 53: ans += "\n"
   return ans
def sudoku_csp():
   return [{0, 1, 2, 3, 4, 5, 6, 7, 8}, {9, 10, 11, 12, 13, 14, 15, 16, 17}, {18, 19, 20, 21, 22, 23, 24, 25, 26}, {32, 33, 34, 35, 27, 28, 29, 30, 31}, {36, 37, 38, 39, 40, 41, 42, 43, 44}, {45, 46, 47, 48, 49, 50, 51, 52, 53}, {54, 55, 56, 57, 58, 59, 60, 61, 62}, {64, 65, 66, 67, 68, 69, 70, 71, 63}, {72, 73, 74, 75, 76, 77, 78, 79, 80}, {0, 36, 72, 9, 45, 18, 54, 27, 63}, {64, 1, 37, 73, 10, 46, 19, 55, 28}, {65, 2, 38, 74, 11, 47, 20, 56, 29}, {66, 3, 39, 75, 12, 48, 21, 57, 30}, {67, 4, 40, 76, 13, 49, 22, 58, 31}, {32, 68, 5, 41, 77, 14, 50, 23, 59}, {33, 69, 6, 42, 78, 15, 51, 24, 60}, {34, 70, 7, 43, 79, 16, 52, 25, 61}, {35, 71, 8, 44, 80, 17, 53, 26, 62}, {0, 1, 2, 9, 10, 11, 18, 19, 20}, {3, 4, 5, 12, 13, 14, 21, 22, 23}, {6, 7, 8, 15, 16, 17, 24, 25, 26}, {36, 37, 38, 45, 46, 47, 27, 28, 29}, {32, 39, 40, 41, 48, 49, 50, 30, 31}, {33, 34, 35, 42, 43, 44, 51, 52, 53}, {64, 65, 72, 73, 74, 54, 55, 56, 63}, {66, 67, 68, 75, 76, 77, 57, 58, 59}, {69, 70, 71, 78, 79, 80, 60, 61, 62}]
   # csp = [[]]
   # for a in range(0, 81, 9):
   #    csp.append({*range(a, a+9)})
   # for a in range(9):
   #    csp.append({*range(a, a+73, 9)})
   # for a in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
   #    csp.append({a, a+1, a+2, a+9, a+10, a+11, a+18, a+19, a+20})
   # return csp[1:]

def initial_variables(puzzle, csp_table): #initializes with variables and their domains
   neighbors = {a : {b for c in csp_table if a in c for b in c} for a in range(81)}
   return {a : {'1','2','3','4','5','6','7','8','9'} - {puzzle[b] for b in neighbors[a]} for a in range(81) if puzzle[a] == '.'}
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   begin = time.time()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   end = time.time()
   print(end - begin)
   
if __name__ == '__main__': main()

