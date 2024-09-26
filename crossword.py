import sys; args = sys.argv[1:]
import re
BLOCKCHAR, OPENCHAR, PROTECTEDCHAR = "#", "-", "~"
width, height, blocks = int(args[0][args[0].index('x')+1:]), int(args[0][0:args[0].index('x')]), int(args[1])
def display(board, width):
    for i in range(len(board)):
       print(board[i], end = '')
       if (i+1) % width == 0: print()
def initialization(args):
    x, y = 0, 0
    if height * width == blocks: ls = [[BLOCKCHAR] * width for i in range(height)]
    else: ls = [[OPENCHAR] * width for i in range(height)]
    c = ""
    for i in args[2:]:
        x = int(i[1:i.index('x')])
        for j in i[i.index('x')+1:]: 
            if j.isnumeric(): c += j
        y, c, word = int(c), "", ""
        if i[0] == 'V' or i[0] == 'v': 
            for j in range(len(i[4:])): 
                if i[4:][j].isnumeric() == False: word += i[4:][j]
            for j in word: ls[(x:=x+1)-1][y] = j
        elif i[0] == 'H' or i[0] == 'h':
            for j in range(len(i[4:])): 
                if i[4:][j].isnumeric() == False: word += i[4:][j]
            for j in word: ls[x][(y:=y+1)-1] = j
    return "".join([str(c) for c in ["".join([str(b) for b in a]) for a in ls]])
def transpose(string):
    ls, n = list(string), len(string) - 1
    for i in range(len(string)//2):
        pair = {ls[i], ls[n-i]}
        if BLOCKCHAR in pair and OPENCHAR in pair: ls[i], ls[n-i] = BLOCKCHAR, BLOCKCHAR
        if PROTECTEDCHAR in pair and OPENCHAR in pair: ls[i], ls[n-i] = PROTECTEDCHAR, PROTECTEDCHAR
    return ''.join(ls)
def horizontal(string):
    ls = [string[i:i+width] for i in range(0, len(string) - width - 1, width)]
    ls = [re.sub('(#(-|~)#)|(^(--|-~|~~)#)|(#(--|-~|~~)$)', '###', a) for a in ls]
    ls = [re.sub('(^(-|~)#)|#(-|~)$', '##', a) for a in ls]
    ls = [re.sub('#(--|-~|~~)#', '####', a) for a in ls]
    return ''.join(ls)
def isValid(string):
    for i, v in enumerate(string):
        if v == '#': continue
        myStr = ''
        if i - 2 >= 0 and (i-2)//width == i//width: myStr += '#' if string[i-2] == '#' else '-'
        if i - 1 >= 0 and (i-1)//width == i//width: myStr += '#' if string[i-1] == '#' else '-'
        if i + 1 < len(string) and (i-2)//width == i//width: myStr += '#' if string[i-2] == '#' else '-'
        if i - 1 >= 0 and (i-1)//width == i//width: myStr += '#' if string[i-1] == '#' else '-'
        if '---' not in myStr: return False
        myStr = ''
        if i - (2 * width) >= 0: myStr += '#' if string[i - (2 * width)] == '#' else '-'
        if i - width >= 0: myStr += '#' if string[i-width] == '#' else '-'
        if i + (2 * width) < len(string): myStr += '#' if string[i+2*width] == '#' else '-'
        if i + width < len(string): myStr += '#' if string[i+width] == '#' else '-'
        if '---' not in myStr: return False 
    j = [a.split("") for a in string]

    temp, a = [], []
    for c in range(len(j)):
        temp.append(c)
        if (c+1) % width == 0: 
            a.append(temp)
            temp = []   
    return True    
def floodfill(i, j, a, count):
    if a[i][j] == PROTECTEDCHAR or a[i][j] == BLOCKCHAR or i < 0 or i >= len(a) or j < 0 or j < len(a[0]): return count
    a[i][j] = PROTECTEDCHAR
    return 1 + floodfill(i-1, j, a, count) + floodfill(i+1, j, a, count) + floodfill(i, j-1, a, count) + floodfill(i, j+1, a, count)
def solve(string):
    return string
def flip(string, width):
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
string = initialization(args)

#print(transpose(initialization(args)))
#Dhruv Anurag 5 2024