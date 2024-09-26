
def problem1(ls):
    return ls.count(19) == 2 and ls.count(5) > 3
def problem2(ls):
    return len(ls) == 8 and ls.count(ls[4]) == 3
def problem3(int):
    return int > 4*4*4*4 and int % 34 == 4
def problem4(int):
    return [i for i in range(int, int * 2 + int, 2)]
def problem5(ls):
    for a in range(1, len(ls)): 
        if (ls[a-1] in ls[a]) == False: return False
    return True
def problem6(ls):
    if len(ls) != 100: return False
    for a in range(1, len(ls)): 
        if(ls[a] - ls[a-1]) != 10: return False
    return True
def problem7(ls):
    return len(ls) == sum(ls)
def problem8(string):
    lss = string.split()
    return [lss, [' '] * (len(lss) - 1)]
def problem9(ls):
    if len(set(ls)) != 4: return False
    for a in range(1, len(ls)): 
        if ls[a] == ls[a-1]: return False
    return True
def problem11(ls):
    threshold, indexes = ls[0][0], []
    for a in range(len(ls[0][1])): 
        if ls[0][1][a] < threshold: indexes.append(a)
    return indexes
def problem12(ls):
    return [i == i[::-1] for i in ls]
def problem13(ls):
    prefix, words = ls[0][0], []
    for a in ls[0][1]: 
        if a.startswith(prefix): words.append(a)
    return words
def problem14(ls):
    return [len(i) for i in ls]
def problem15(ls):
    max = ""
    for a in ls: 
        if len(a) > len(max): max = a
    return a
def problem16(ls):
    contained, words = ls[0][0], []
    for a in ls[0][1]: 
        if contained in a: words.append(a)
    return words
def problem17(int):
    string = "0 "
    for a in range(1, int+1): string += str(a) + " "
    string = string[:-1]
    return string
def problem18(ls):
    contains, tuples = ls[1], ls[0]
    print(tuples)
    temp, ls = [], []
    for a in tuples: 
        for b in range(len(a)):
            if a[b] == contains: temp.append(b)
        ls.append(temp)
        temp = []
    return ls
def problem19(string):
    if " " in string: return string.split()
    if "," in string: return string.split(",")
def problem20(ls):
    curr = ""
    for a in range(1, len(ls)):
        if a == 1 and ls[a] > ls[a-1]: 
            curr = "increasing"
            continue
        if a == 1 and ls[a] < ls[a-1]: 
            curr = "decreasing"
            continue
        if a == 1 and ls[a] == ls[a-1]: return "Not a monotonic sequence!"
        if ls[a] > ls[a-1] and curr == "decreasing": return "Not a monotonic sequence!"
        if ls[a] < ls[a-1] and curr == "increasing": return "Not a monotonic sequence!"
    return curr
def problem21(ls):
    return [a[-2] == " " for a in ls]
def problem22(ls):
    return sum([ord(a) for a in ls if a.upper() == a and a.isalpha() == True])
def problem23(ls):
    temp = []
    for a in range(1, len(ls)):
        if(ls[a-1] > ls[a]): temp.append(a)
    return temp
def problem24(ls):
    temp, max = [], -10000
    for a in range(len(ls)):
        if ls[a] > max: 
            max = ls[a]
        temp.append(max)
    return temp
def problem25(ls):
    return bin(int(ls[0], 2) ^ int(ls[1], 2))
def problem26(ls):
    temp, b = [], 0
    for a in ls:
        if "," in a: 
            a = a[:a.index(',')] + '.' + a[a.index(',')+1:]
        temp.append(float(a))
    return max(temp)
def problem27(ls):
    return sum(ls)/len(ls)
def problem28(ls):
    temp, chars, max, maxstring = [], 0, 0, ""
    for a in ls:
        chars = len(set([b for b in a]))
        if chars > max: 
            max = chars
            maxstring = a
    return maxstring
def problem29(ls):
    for a in ls:
        if (-1 * a) in ls: return [ls.index(a), ls.index(-1 * a)]
    return "No pair found!"
def problem30(ls):
    print(''.join(a for a in ls[0]))
    one = len(''.join(a for a in ls[0]))
    two = len(''.join(a for a in ls[1]))
    if one > two: return ls[0]
    else: return ls[1]

    



        
 