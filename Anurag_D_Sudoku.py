# Name: Dhruv Anurag
# Date: 11/10/21
import random
def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for hexa in csp_table:
      if len(set([assignment[i] for i in hexa])) != 6: return False
   return True
   
def select_unassigned_var(assignment, csp_table):
   """ your code goes here """
   if assignment.find('.') == -1: return -1
   return random.choice([a for a in range(81) if assignment[a] == '.'])
   
def isValid(value, var_index, assignment, csp_table):
   """ your code goes here """
   if var_index == -1: return False
   for a in range(len(csp_table)):
      for b in csp_table[a]:
         if var_index in csp_table[a] and assignment[b] == value:
            return False
   return True

def backtracking_search(input, csp_table): 
   return recursive_backtracking(input, csp_table)

def recursive_backtracking(assignment, csp_table):
   """ your code goes here """
   if check_complete(assignment, csp_table): return assignment
   var = select_unassigned_var(assignment, csp_table)
   for a in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      if isValid(a, var, assignment, csp_table):
         assignment = assignment[:var] + a + assignment[var+1:]
         r = recursive_backtracking(assignment, csp_table)
         if r != None:
            return r
   return None

def display(solution):
   result = ""
   for i in range(len(solution)):
      if i == 0: result += "  "
      if i == 5: result += "\n"
      if i == 12: result += "\n"
      if i == 19: result += "\n  "
      result += solution[i] + " "
   return result

def main():
  #csp_table = [[0, 1, 2, 3, 4, 5 ,]]
   csp_table = []
   solution = backtracking_search(input("24-char(. and 1-6) input: "), csp_table)
   if solution != None:
      print (display(solution))
      print ('\n'+ solution)
      print (check_complete(solution, csp_table))
   else: print ("It's not solvable.")

if __name__ == '__main__':
   main()
   
"""
Sample Output 1:
24-char(. and 1-6) input: ........................
  1 2 3 1 2 
1 4 5 6 4 5 1 
2 6 3 1 2 3 6 
  2 4 5 4 6 

123121456451263123624546
True

Sample Output 2:
24-char(. and 1-6) input: 6.....34...1.....2..4...
  6 1 2 1 3 
1 3 4 5 6 4 1 
5 6 2 1 3 2 5 
  3 4 5 4 6 

612131345641562132534546
True
"""