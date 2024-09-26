import sys

from numpy import block; args = sys.argv[1:]
import re
BLOCKCHAR, OPENCHAR, PROTECTEDCHAR = '#', '-', '~'
width, height, blocks = int(args[0][args[0].index('x')+1:]), int(args[0][0:args[0].index('x')]), int(args[1])

def initialization(args):
    x, y = 0, 0
    if height * width == blocks: ls = [[BLOCKCHAR] * width for i in range(height)]
    else: ls = [[OPENCHAR] * width for i in range(height)]
    c = ""
    for i in args[2:]:
        x = int(i[1:i.index('x')])
        for j in i[i.index('x')+1:]: 
            if j in '0 1 2 3 4 5 6 7 8 9'.split(): c += j
        y, c, word = int(c), "", ""
        if i[0] == 'V' or i[0] == 'v': 
            for j in range(len(i[4:])): 
                if i[4:][j] not in '0 1 2 3 4 5 6 7 8 9'.split(): word += i[4:][j]
            for j in word: 
                ls[x][y] = j
                x += 1
        elif i[0] == 'H' or i[0] == 'h':
            for j in range(len(i[4:])): 
                if i[4:][j] not in '0 1 2 3 4 5 6 7 8 9'.split(): word += i[4:][j]
            for j in word: 
                ls[x][y] = j
                y += 1
    myStr = "".join([str(c) for c in ["".join([str(b) for b in a]) for a in ls]])
    newStr = ''
    for a in myStr:
        newStr += PROTECTEDCHAR if a.lower() in 'abcdefghijklmnopqrstuvwxyz' else a
    display(newStr, height, width)
    return myStr, newStr

def display(xword, height, width):
    #print(xword)
    print('\n'.join([xword[width*k:width*(k+1)] for k in range(height)]))
   # print('\n'.join([xword[width*k:width*(k+1)] for k in range(height)]), end = '\n\n')

def initialboard(xword):
    xword_list, temp = list(xword), []
    for x in xword_list:
        if x not in {OPENCHAR, BLOCKCHAR}: temp.append('~')
        else: temp.append(x)
    return ''.join(temp)

def make_palindrome(xword):
    xword_list, n = list(xword), len(xword) - 1
    for i in range(len(xword_list)//2):
        pair = {xword_list[i], xword_list[n-i]}
        if BLOCKCHAR in pair and OPENCHAR in pair: xword_list[i], xword_list[n-i] = BLOCKCHAR, BLOCKCHAR
        elif PROTECTEDCHAR in pair and OPENCHAR in pair: xword_list[i], xword_list[n-i] = PROTECTEDCHAR, PROTECTEDCHAR
    #print(''.join(xword_list))
    return ''.join(xword_list)

def isValid(string):
    checked = area_fill(string, min(string.index('-'), string.index('~') if '~' in string else len(string)))
    if checked.count('?') != string.count("-") + string.count("~"): return False
    return True

def area_fill(board, sp, dirs = [-1, width, 1, -1 * width]):
    if sp < 0 or sp >= len(board): return board
    if board[sp] in {OPENCHAR, PROTECTEDCHAR}:
        board = board[:sp] + '?' + board[sp+1:]
        for d in dirs:
            if d == -1 and sp % width == 0: continue
            if d == 1 and sp+1 % width == 0: continue
            board = area_fill(board, sp+d, dirs)
    return board

def add_blocks(board, blockcount, height, width):
    string = ""
    for a in board: string += "~" if a in 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split() else a
    board = string
    new_board = make_palindrome(board)
   # print(new_board)
    while new_board != None and new_board.count(BLOCKCHAR) < blocks or isValid(new_board) == False:
        new_board, num_of_blocks = 0, 0
        new_board = add_helper(board, num_of_blocks)
    return new_board

def add_helper(board, curr_num_of_blocks):
    if curr_num_of_blocks == blocks: 
        print("HI")
        return board, curr_num_of_blocks
    new_board, found = [], False
    pos_list = {a for a in range(len(board)) if board[a] == OPENCHAR}
    for a in pos_list:
        new_board = board[:a] + BLOCKCHAR + board[a+1:]
        if isValid(new_board): 
            found = True
            break
        else: 
            new_board = board[:a] + PROTECTEDCHAR + board[a+1:]
    if found == False: return;
    new, temp = block_helper(new_board)
    print(new)
    new_board = make_palindrome(new)
    board = new_board
    return add_helper(board, curr_num_of_blocks)


def transpose(string, width):
    matrix, temp = [], []
    for a in range(len(string)):
        temp.append(string[a])
        if (a+1) % width == 0: 
            matrix.append(temp)
            temp = []
    rows, columns, matrix_T = len(matrix), len(matrix[0]), []
    for j in range(columns):
        row = []
        for i in range(rows): row.append(matrix[i][j])
        matrix_T.append(row)
    return "".join([str(c) for c in ["".join([str(b) for b in a]) for a in matrix_T]])


def block_helper(board):
    xw = BLOCKCHAR*(width+3) + (BLOCKCHAR*2).join([board[p:p+width] for p in range(0, len(board), width)]) + BLOCKCHAR * (width + 3)
    print(xw)
    ilegRE = '[{}].?[{}][{}]'.format(BLOCKCHAR, PROTECTEDCHAR, BLOCKCHAR)
    newH = len(xw) // (width+2)
    display(xw, width+2, height+2)
    for turn in range(2):
        if re.search(ilegRE, xw): return board, len(board)
        xw = transpose(xw, len(xw) // newH)
        newH = len(xw) // newH
    subRE = "[{}]{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, BLOCKCHAR)
    subRE2 = "[{}]{}{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, OPENCHAR, BLOCKCHAR)
    subRE3 = "[#](-~-|--~|~--|~~-|-~~|~-~)(?=[#])"
    newH = len(xw) // (width+2)
    for turn in range(2):
        if re.search(ilegRE, xw): return board, len(board)
        xw = re.sub(subRE, BLOCKCHAR*2, xw)
        xw = re.sub(subRE2, BLOCKCHAR*2, xw)
        xw = re.sub(subRE3, BLOCKCHAR + PROTECTEDCHAR*3, xw)
        xw = transpose(xw, len(xw)//newH)
        newH = len(xw)//newH
    new_board = ''
    for row in range(width+2, len(xw) - (width+2), width+2): new_board += xw[row+1:width+row+1]
    #display(new_board, height, width)
    return new_board, new_board.count(BLOCKCHAR)

def main():
    # temp, board = initialization(args)
    # board = add_blocks(board, blocks, height, width)
    # print(isValid(board))
    board = '------------'
    board, temp = block_helper(board)
    #display(board, width, height)

if __name__ == "__main__":
    main()






