count = 0
def solve(line):
    li = list(line.strip())
    fibSeq, count = genFibonacciSeq(int(li[0]), int(li[2]), len(li) - 6), 0
    decoded = []
    for i in li[6:]:
        decoded.append((ord(makeDict(fibSeq[count])[li[4]])) * 3 + ord(i))
        count += 1
    return decoded
def genFibonacciSeq(one, two, length):
    fib = [one, two]
    for a in range(length - 2):
        if(len(fib) % 20 == 0):
            fib.append(one)
            fib.append(two)
            a += 1
            continue
        fib.append(fib[len(fib) - 2] + fib[len(fib) - 1])
    return fib
def makeDict(number):
    li, dic = 'abcdefghijklmnopqrstuvwxyz', dict()
    dic = {li[i] : li[(i+number)%26] for i in range(26)}
    return dic
with open('test.txt', 'r') as file:
    for line in file:
        print(str((count := count + 1)) + '.', end = ' ') 
        for a in solve(line):
            print(a, end = ' ')
        print()