a = input("list of numbers: ").split(" ")
a = [int(b) for b in a]
print(sum(a))

print([x for x in a if x % 3 == 0])
def fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(1,int(input("Type n for Fibonacci sequence: "))+1): 
    print(str(fibonacci(i)), end = " ")
print()

print(input("Type a string: ")[::2])

def prime(n):
    for i in range(2, int(n/2+2)):
        if n % i == 0:
            return False
    return True
print(prime(int(input("Type a number to check prime: "))))

a = input("Type three sides of a triangle: ").split(" ")
a = [int(x) for x in a]
print((sum(a)/2 * (sum(a)/2 - a[0]) * (sum(a)/2 - a[1]) * (sum(a)/2 - a[2])) ** 0.5)

a = list(input("Type a sentence: "))
a = [x for x in a if x not in ('?','.',',',';',':','"',"'",'!','-','{','}','[',']','(',')',' ')]
b = ''.join(x for x in a)
print(b)

print(b.lower() == b[::-1].lower())

print({'a':b.count('a'), 'e':b.count('e'), 'i':b.count('i'), 'o':b.count('o'), 'u':b.count('u')})

a = input("Type two integers (lower bound and upper bound): ").split(" ")
for i in range(int(a[0]), int(a[1])+1) :
    print((i**2)-(3*i)+2, end = ' ')
print()


a = {}
s = input("Type a string: ")
import collections
s = s.replace(" ", "")
largest_count: int = collections.Counter(s).most_common()[0][1]
most_common_list: list = [x
    for x, y in collections.Counter(s).items() if y == largest_count]
for a in most_common_list:
    print(a, end = ' ')
print()


b = s.split(" ")
z = s.split(" ")
c = [x for x in b if x.startswith(('a','e','i','o','u')) and x.endswith(('a','e','i','o','u'))]
print(c)
print(s.title())
print(' '.join(b:=[x[::-1] for x in b]))
if len(z) >= 2:
    s = s.replace(z[0], z[1]) 
w = s.split(" ")
print(' '.join(w[2:]))
a = input("Type a string to remove all duplicate chars: ")
print(''.join(dict.fromkeys(a)))
from PIL import Image
a = input("Type a string to check if it has only digits or not: ")
print(len(a) == sum(x in ('1','2','3','4','5','6','7','8','9','0') for x in a))
if(len(a) == sum(x in ('1','0') for x in a)):
    print(int(a, 2))
else:
    print("Not a binary number")
s1 = input("Type the first string to check anagram: ")
s2 = input("Type the second string to check anagram: ")
print(sorted(s1) == sorted(s2))
try:
    img = Image.open(input("Type the image file name: "))
    width, height = img.size
    print(str(width) + " by " + str(height))
except FileNotFoundError:
    pass

s = input("Type a string to find the longest palindrome: ")
s = s.replace(" ", "")
s1 = '|' + ''.join(a + '|' for a in list(s))
slist = [0] * len(s1)
center = 0
temp = ''
while center < len(s1):
    radius = 0
    while center - radius + 1 >= 0 and center + (radius+1) < len(s1) and s1[center-radius-1] == s1[center+radius+1]:
        radius += 1
    if radius > max(slist):
        temp = s1[center-radius:center+radius+1]
    slist[center] = radius
    center += 1
print(temp.replace("|",""))

from itertools import permutations
s = input("Type a string to do permutation: ")
print([''.join(a) for a in list(permutations(s))])
print(set([''.join(a) for a in list(permutations(s))]))

s = input("Type a string to find the longest non-decreasing sub: ")
s = s.replace(" ","")
ls = [""]*20
count = 0
for i in range(1, len(s)):
    if ord(s[i-1]) <= ord(s[i]):
        ls[count] += s[i]
    else:
        count += 1
        ls[count] = s[i]
max = 0
for i in range(len(ls)):
    if len(ls[i]) >= max:
        max = i
print(ls[max])


