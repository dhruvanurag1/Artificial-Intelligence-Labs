# Name: Alina Chen
# Date: 12/22/2022

import random

class RandomPlayer:
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
      moves = self.find_moves(board, color)
      best_move = moves[random.randint(0, len(moves) - 1)]
      flipped_stones = self.find_flipped(board, best_move[0], best_move[1], color)
      for i in flipped_stones:
         board[i[0][1]] = color
      if (color == "#000000"):
         return best_move, 0
      else:
         return best_move, 1

   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      stones_left = 0
      for i in range(board):
         for j in range(board[0]):
            if (board[i][j] == '.'):
               stones_left += 1
      return stones_left

   def find_moves(self, board, color):
    # finds all possible moves
      moves = {}
      for i in range(len(board)):
         for j in range(len(board[0])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if (len(flipped_stones) > 0):
               moves.update({i * self.y_max + j: flipped_stones})
      return moves

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      if (board[x][y] != '.'):
         return []
      if (color == self.black):
         color = "@"
      else:
         color = "O"
      flipped_stones = []
      for i in self.directions:
         temp = []
         x_pos = x + i[0]
         y_pos = y + i[1]
         while (0 <= x_pos < self.x_max) and (0 <= y_pos < self.y_max):
            if (board[x_pos][y_pos] == "."):
               break
            temp.append([x_pos, y_pos])
            x_pos += i[0]
            y_pos += i[1]
            #print(board[x_pos, y_pos], color, self.opposite_color)
            if (board[x_pos][y_pos] == self.opposite_color):
               flipped_stones += temp
      print(flipped_stones)
      return flipped_stones

class CustomPlayer:

   def __init__(self):
      self.white = "#ffffff"
      self.black = "#000000"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.color = None
      self.table = [[999, -3, 2, 2, 2, 2, -3, 999], [-3, -4, -1, -1, -1, -1, -4, -3], [2, -1, 1, 0, 0, 1, -1, 2], [2, -1, 0, 1, 1, 0, -1, 2], [2, -1, 0, 1, 1, 0, -1, 2], [2, -1, 1, 0, 0, 1, -1, 2], [-3, -4, -1, -1, -1, -1, -4, -3], [999, -3, 2, 2, 2, 2, -3, 999]]

   def best_strategy(self, board, color):
    # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      self.color = color
      if (self.stones_left(board) > 32):
         x = 4
      elif (self.stones_left(board) > 10):
         x = 6
      else:
         x = 8
      value, best_move = self.alphabeta(board, color, search_depth = x, alpha = -999999, beta = 999999)
      return (best_move // self.x_max, best_move % self.y_max), 0

   def minimax(self, board, color, search_depth):
    # returns best "value"
      return self.best_strategy(self, board, color)

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return self.best_strategy(self, board, color)
      
   def alphabeta(self, board, color, search_depth, alpha, beta, last_move = -1):
    # returns best "value" while also pruning
      if (search_depth <= 0) or ((self.stones_left(board) == 0)):
         if ((self.stones_left(board) == 0)):
            return self.evaluate(board, self.color, last_move) * 1000000, last_move
         return self.evaluate(board, self.color, last_move), 0
      if (search_depth % 2 == 0):
         value = -999999
         result = 0
         for move, flipped in self.find_moves(board, color).items():
            max_val, max_state = self.alphabeta(self.make_move(board, color, move, flipped), self.opposite_color[color], search_depth - 1, alpha, beta, move)
            if (value < max_val):
               value = max_val
               result = move
            if (value > beta):
               return value, result
            alpha = max(alpha, value)
         return value, result
      else:
         value = 999999
         result = 0
         for move, flipped in self.find_moves(board, color).items():
            min_val, min_state = self.alphabeta(self.make_move(board, color, move, flipped), self.opposite_color[color], search_depth - 1, alpha, beta, move)
            if (value > min_val):
               value = min_val
               result = move
            if (value < alpha):
               return value, result
            beta = min(beta, value)
         return value, result

   def make_key(self, board, color):
    # hashes the board
      return self.best_strategy(self, board, color)

   def stones_left(self, board):
    # returns number of stones that can still be placed
      stones_left = 0
      for i in range(len(board)):
         for j in range(len(board[0])):
            if (board[i][j] == "."):
               stones_left += 1
      return stones_left

   def make_move(self, board, color, move, flipped):
    # returns board that has been updated
      my_board = [row[:] for row in board]
      if (color == self.black):
         color = "@"
      else:
         color = "O"
      my_board[move // self.x_max][move % self.y_max] = color
      for i in flipped:
         my_board[i[0]][i[1]] = color
      return my_board

   def evaluate(self, board, color, last_move):
    # returns the utility value
      score = self.score(board, color)
      if (last_move != -1):
         heuristic = self.table[last_move // self.x_max][last_move % self.y_max]
         return score * heuristic
      else:
         return score

   def score(self, board, color):
    # returns the score of the board 
      if (color == self.black):
         color = "@"
      else:
         color = "O"
      score = 0
      for i in range(len(board)):
         for j in range(len(board[0])):
            if (board[i][j] == color):
               score += 1
            elif (board[i][j] != '.'):
               score -= 1
      return score

   def find_moves(self, board, color):
    # finds all possible moves
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[0])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if (len(flipped_stones) > 0):
               moves_found.update({i * self.y_max + j: flipped_stones})
      return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      if (board[x][y] != '.'):
         return []
      if (color == self.black):
         color = "@"
      else:
         color = "O"
      flipped_stones = []
      for i in self.directions:
         temp = []
         x_pos = x + i[0]
         y_pos = y + i[1]
         while (0 <= x_pos < self.x_max) and (0 <= y_pos < self.y_max):
            if (board[x_pos][y_pos] == "."):
               break
            if (board[x_pos][y_pos] == color):
               flipped_stones += temp
               break
            temp.append([x_pos, y_pos])
            x_pos += i[0]
            y_pos += i[1]
      print(flipped_stones)
      return flipped_stones