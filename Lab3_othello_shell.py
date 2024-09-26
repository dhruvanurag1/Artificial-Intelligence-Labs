# Name: Dhruv Anurag
# Date: 1/12/21

import random

class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here ''' 
      return ((v:=random.choice(list(self.find_moves(board, color).keys())))//5, v%5), 0

   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == '.': count += 1
      return count

   def find_moves(self, board, color):
    # finds all possible moves
      moves_found = dict()
      for i in range(len(board)):
         for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found[i*self.y_max+j] = flipped_stones
      print(moves_found)
      print('\n\n\n')
      return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
    if board[x][y] != ".":
            return []
    if color == self.black:
        my_color = "@"
    else:
        my_color = "O"
    flipped_stones = []
    for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
                break
            if board[x_pos][y_pos] == my_color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
    return flipped_stones

class Best_AI_bot:

   def __init__(self):
      self.white = "o"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
    # returns best move
      return best_move, 0

   def minimax(self, board, color, search_depth):
    # returns best "value"
      return 1

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning
      pass

   def make_key(self, board, color):
    # hashes the board
      return 1

   def stones_left(self, board):
    # returns number of stones that can still be placed
      return 1

   def make_move(self, board, color, move, flipped):
    # returns board that has been updated
      return 1

   def evaluate(self, board, color, possible_moves):
    # returns the utility value
      return 1

   def score(self, board, color):
    # returns the score of the board 
      return 1

   def find_moves(self, board, color):
    # finds all possible moves
      return 1

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      return 1
