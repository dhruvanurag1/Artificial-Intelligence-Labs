def factorial(a): return 1 if a == 0 or a == 1 else factorial(a-1) * a
def solve(a):
    summation, seq, row, column, init_row, second_seq = 0, [], 1, 0, 0, []
    while True == True:
      row, seq, column, second_seq = init_row, [], init_row, []
      while column >= 0: seq.append(factorial((row:=row+1)-1)/(factorial((column:=column-1)+1)*factorial(row - column - 2)))
      column, row = init_row - 1, (init_row:=init_row+1) - 1
      while column >= 0: second_seq.append(factorial((row:=row+1)-1)/(factorial((column:=column-1)+1)*factorial(row - column - 2)))
      if sum(seq) == a: return seq
      if sum(second_seq) == a: return second_seq
for b, a in enumerate(open('test.txt', 'r').read().splitlines()): print(str(b+1) + '.', sum([1 for b in solve(int(a)) if b % 2 == 1]), sum([1 for b in solve(int(a)) if b % 2 == 0]), int(max(solve(int(a)))))