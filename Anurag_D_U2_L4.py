import sys; args = sys.argv[1:]
puzzles = open('/Users/dhruvanurag/Documents/TJ/AI/puzzles.txt', "r").read().splitlines()
import time

def solve(puzzle, neighbors):
   # initialize_ds function is optional helper function. You can change this part. 
   return recursive_backtracking(puzzle, {a : {'1','2','3','4','5','6','7','8','9'} - {puzzle[b] for b in neighbors[a]} for a in range(81) if puzzle[a] == '.'}, neighbors)

# optional helper function: you are allowed to change it
def recursive_backtracking(assignment, variables, neighbors):
   ''' Your code goes here'''
   if assignment.find('.') == -1: return assignment
   for a in variables[(var := list(variables.keys())[list(variables.values()).index(min(variables.values(), key = len))])]:
      if assignment.count(a) == 9: continue
      elif (tempvariables := {key : variables[key] - {a} if key in neighbors[var] else variables[key] for key in variables if key != var} if len({True for c in neighbors[var] if c != var and (assignment := assignment[:var] + a + assignment[var+1:])[c] == a}) == 0 else None) != None:
         if (r := recursive_backtracking(assignment, tempvariables, neighbors)) != None: return r
   return None
def sudoku_csp(n=9):
   ''' Your code goes here '''
   # return [{*range(a, a+9)} for a in range(0, 73, 9)] + [{*range(a, a+73, 9)} for a in range(9)] + [{a, a+1, a+2, a+9, a+10, a+11, a+18,a+19,a+20} for a in [0,3,6,27,30,33,54,57,60]]
   return [{0, 1, 2, 3, 4, 5, 6, 7, 8}, {9, 10, 11, 12, 13, 14, 15, 16, 17}, {18, 19, 20, 21, 22, 23, 24, 25, 26}, {32, 33, 34, 35, 27, 28, 29, 30, 31}, {36, 37, 38, 39, 40, 41, 42, 43, 44}, {45, 46, 47, 48, 49, 50, 51, 52, 53}, {54, 55, 56, 57, 58, 59, 60, 61, 62}, {64, 65, 66, 67, 68, 69, 70, 71, 63}, {72, 73, 74, 75, 76, 77, 78, 79, 80}, {0, 36, 72, 9, 45, 18, 54, 27, 63}, {64, 1, 37, 73, 10, 46, 19, 55, 28}, {65, 2, 38, 74, 11, 47, 20, 56, 29}, {66, 3, 39, 75, 12, 48, 21, 57, 30}, {67, 4, 40, 76, 13, 49, 22, 58, 31}, {32, 68, 5, 41, 77, 14, 50, 23, 59}, {33, 69, 6, 42, 78, 15, 51, 24, 60}, {34, 70, 7, 43, 79, 16, 52, 25, 61}, {35, 71, 8, 44, 80, 17, 53, 26, 62}, {0, 1, 2, 9, 10, 11, 18, 19, 20}, {3, 4, 5, 12, 13, 14, 21, 22, 23}, {6, 7, 8, 15, 16, 17, 24, 25, 26}, {36, 37, 38, 45, 46, 47, 27, 28, 29}, {32, 39, 40, 41, 48, 49, 50, 30, 31}, {33, 34, 35, 42, 43, 44, 51, 52, 53}, {64, 65, 72, 73, 74, 54, 55, 56, 63}, {66, 67, 68, 75, 76, 77, 57, 58, 59}, {69, 70, 71, 78, 79, 80, 60, 61, 62}]

def sudoku_neighbors(csp_table): # {0:[0, 1, 2, 3, 4, ...., 8, 9, 18, 27, 10, 11, 19, 20], 1:
   ''' Your code goes here '''
   #return {a : {c for table in csp_table if a in table for c in table} for a in range(81)}
   return {0: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 27, 36, 45, 54, 63, 72}, 1: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 28, 37, 46, 55, 64, 73}, 2: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 29, 38, 47, 56, 65, 74}, 3: {0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 21, 22, 23, 30, 39, 48, 57, 66, 75}, 4: {0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 21, 22, 23, 31, 40, 49, 58, 67, 76}, 5: {0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 21, 22, 23, 32, 41, 50, 59, 68, 77}, 6: {0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 17, 24, 25, 26, 33, 42, 51, 60, 69, 78}, 7: {0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 17, 24, 25, 26, 34, 43, 52, 61, 70, 79}, 8: {0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 17, 24, 25, 26, 35, 44, 53, 62, 71, 80}, 9: {0, 1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 36, 45, 54, 63, 72}, 10: {0, 1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 28, 37, 46, 55, 64, 73}, 11: {0, 1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 29, 38, 47, 56, 65, 74}, 12: {3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 30, 39, 48, 57, 66, 75}, 13: {3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 31, 40, 49, 58, 67, 76}, 14: {3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 32, 41, 50, 59, 68, 77}, 15: {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 24, 25, 26, 33, 42, 51, 60, 69, 78}, 16: {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 24, 25, 26, 34, 43, 52, 61, 70, 79}, 17: {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 24, 25, 26, 35, 44, 53, 62, 71, 80}, 18: {0, 1, 2, 9, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 36, 45, 54, 63, 72}, 19: {0, 1, 2, 9, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 37, 46, 55, 64, 73}, 20: {0, 1, 2, 9, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 38, 47, 56, 65, 74}, 21: {3, 4, 5, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 30, 39, 48, 57, 66, 75}, 22: {3, 4, 5, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 31, 40, 49, 58, 67, 76}, 23: {3, 4, 5, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 32, 41, 50, 59, 68, 77}, 24: {6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 33, 42, 51, 60, 69, 78}, 25: {6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 34, 43, 52, 61, 70, 79}, 26: {6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 35, 44, 53, 62, 71, 80}, 27: {0, 9, 18, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 54, 63, 72}, 28: {1, 10, 19, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 55, 64, 73}, 29: {2, 11, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 56, 65, 74}, 30: {3, 12, 21, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 40, 41, 48, 49, 50, 57, 66, 75}, 31: {4, 13, 22, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 40, 41, 48, 49, 50, 58, 67, 76}, 32: {5, 14, 23, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 40, 41, 48, 49, 50, 59, 68, 77}, 33: {6, 15, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 51, 52, 53, 60, 69, 78}, 34: {7, 16, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 51, 52, 53, 61, 70, 79}, 35: {8, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 51, 52, 53, 62, 71, 80}, 36: {0, 9, 18, 27, 28, 29, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 54, 63, 72}, 37: {1, 10, 19, 27, 28, 29, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 55, 64, 73}, 38: {2, 11, 20, 27, 28, 29, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 56, 65, 74}, 39: {3, 12, 21, 30, 31, 32, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 57, 66, 75}, 40: {4, 13, 22, 30, 31, 32, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 58, 67, 76}, 41: {5, 14, 23, 30, 31, 32, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 59, 68, 77}, 42: {6, 15, 24, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 52, 53, 60, 69, 78}, 43: {7, 16, 25, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 52, 53, 61, 70, 79}, 44: {8, 17, 26, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 52, 53, 62, 71, 80}, 45: {0, 9, 18, 27, 28, 29, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 63, 72}, 46: {1, 10, 19, 27, 28, 29, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 64, 73}, 47: {2, 11, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 56, 65, 74}, 48: {3, 12, 21, 30, 31, 32, 39, 40, 41, 45, 46, 47, 48, 49, 50, 51, 52, 53, 57, 66, 75}, 49: {4, 13, 22, 30, 31, 32, 39, 40, 41, 45, 46, 47, 48, 49, 50, 51, 52, 53, 58, 67, 76}, 50: {5, 14, 23, 30, 31, 32, 39, 40, 41, 45, 46, 47, 48, 49, 50, 51, 52, 53, 59, 68, 77}, 51: {6, 15, 24, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 69, 78}, 52: {7, 16, 25, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 61, 70, 79}, 53: {8, 17, 26, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 62, 71, 80}, 54: {0, 9, 18, 27, 36, 45, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 72, 73, 74}, 55: {1, 10, 19, 28, 37, 46, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 72, 73, 74}, 56: {2, 11, 20, 29, 38, 47, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 72, 73, 74}, 57: {3, 12, 21, 30, 39, 48, 54, 55, 56, 57, 58, 59, 60, 61, 62, 66, 67, 68, 75, 76, 77}, 58: {4, 13, 22, 31, 40, 49, 54, 55, 56, 57, 58, 59, 60, 61, 62, 66, 67, 68, 75, 76, 77}, 59: {5, 14, 23, 32, 41, 50, 54, 55, 56, 57, 58, 59, 60, 61, 62, 66, 67, 68, 75, 76, 77}, 60: {6, 15, 24, 33, 42, 51, 54, 55, 56, 57, 58, 59, 60, 61, 62, 69, 70, 71, 78, 79, 80}, 61: {7, 16, 25, 34, 43, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 69, 70, 71, 78, 79, 80}, 62: {8, 17, 26, 35, 44, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 69, 70, 71, 78, 79, 80}, 63: {0, 9, 18, 27, 36, 45, 54, 55, 56, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74}, 64: {1, 10, 19, 28, 37, 46, 54, 55, 56, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74}, 65: {2, 11, 20, 29, 38, 47, 54, 55, 56, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74}, 66: {3, 12, 21, 30, 39, 48, 57, 58, 59, 63, 64, 65, 66, 67, 68, 69, 70, 71, 75, 76, 77}, 67: {4, 13, 22, 31, 40, 49, 57, 58, 59, 63, 64, 65, 66, 67, 68, 69, 70, 71, 75, 76, 77}, 68: {5, 14, 23, 32, 41, 50, 57, 58, 59, 63, 64, 65, 66, 67, 68, 69, 70, 71, 75, 76, 77}, 69: {6, 15, 24, 33, 42, 51, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 78, 79, 80}, 70: {7, 16, 25, 34, 43, 52, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 78, 79, 80}, 71: {8, 17, 26, 35, 44, 53, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 78, 79, 80}, 72: {0, 9, 18, 27, 36, 45, 54, 55, 56, 63, 64, 65, 72, 73, 74, 75, 76, 77, 78, 79, 80}, 73: {1, 10, 19, 28, 37, 46, 54, 55, 56, 63, 64, 65, 72, 73, 74, 75, 76, 77, 78, 79, 80}, 74: {2, 11, 20, 29, 38, 47, 54, 55, 56, 63, 64, 65, 72, 73, 74, 75, 76, 77, 78, 79, 80}, 75: {3, 12, 21, 30, 39, 48, 57, 58, 59, 66, 67, 68, 72, 73, 74, 75, 76, 77, 78, 79, 80}, 76: {4, 13, 22, 31, 40, 49, 57, 58, 59, 66, 67, 68, 72, 73, 74, 75, 76, 77, 78, 79, 80}, 77: {5, 14, 23, 32, 41, 50, 57, 58, 59, 66, 67, 68, 72, 73, 74, 75, 76, 77, 78, 79, 80}, 78: {6, 15, 24, 33, 42, 51, 60, 61, 62, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80}, 79: {7, 16, 25, 34, 43, 52, 60, 61, 62, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80}, 80: {8, 17, 26, 35, 44, 53, 60, 61, 62, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80}}

# sum of all ascii code of each char - (length of the solution * ascii code of min char)
def checksum(solution):
   ''' write your code here'''
   return sum(ord(a) for a in solution) - (81 * 49)

def main():
   csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(csp_table)   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   start_time = time.time()
   for line, puzzle in enumerate(puzzles):
      line, puzzle = line+1, puzzle.rstrip()
      print ("{}: {}".format(line, puzzle)) 
      solution = solve(puzzle, neighbors)
      if solution == None:print ("No solution found."); break
      print ("{}{} {}".format(" "*(len(str(line))+2), solution, checksum(solution)))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
# Required comment: Your name, Period #, 2022
# Check the example below. You must change the line below before submission.
# Dhruv Anurag, Period 5, 2022