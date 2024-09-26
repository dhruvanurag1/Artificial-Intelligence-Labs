def string_times(str, n):
  return n * str
def front_times(str, n): 
  return str[:3]*n
def string_bits(str): 
  return str[::2]
def string_splosion(str):
  return ''.join(str[:i] for i in range(len(str)+1))  
def last2(str): 
  return sum(str[i:i+2]==str[-2:] for i in range(len(str)-3))
def array_count9(nums): 
  return nums.count(9)
def array_front9(nums): 
  return 9 in nums[:4]
def array123(nums): 
  return (1,2,3) in zip(nums,nums[1:],nums[2:])
def string_match(a, b): 
  return sum(a[x:x+2] == b[x:x+2] for x in range(min(len(a),len(b))-1))
def make_bricks(small, big, goal):
  return goal - 5 * min(big, goal // 5) <= small
def lone_sum(a, b, c):
  return sum(i for i in [a,b,c] if [a,b,c].count(i) < 2)
def lucky_sum(a, b, c):
  return sum([a,b,c][:[-1, [a,b,c].index(13)][13 in [a,b,c]]])
def no_teen_sum(a, b, c):
  return sum(z for z in [a,b,c] if z not in (13,14,17,18,19))
def round_sum(a, b, c):
  return sum(int(round(a+.5, -1)) for a in [a,b,c])
def close_far(a, b, c):
  return sum(x<2 for x in [abs(a-b), abs(a-c), abs(b-c)]) ==1 #[a,a+b,a+c,a][]
def make_chocolate(small, big, goal):
  return [goal - 5 * min(big, goal // 5),-1][goal - 5 * min(big, goal // 5) > small]
def double_char(str):
  return ''.join(c+c for c in str)
def count_hi(str):
  return str.count("hi")
def cat_dog(str):
  return str.count("cat") == str.count("dog")
def count_code(str):
  return list(zip(str,str[1:],str[3:])).count(("c","o","e"))
def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())
def xyz_there(str):
  return str.count("xyz") > str.count(".xyz")
def count_evens(nums):
  return sum(i % 2 == 0 for i in nums)
def big_diff(nums):
  return max(nums)-min(nums)
def centered_average(nums):
  return sum(sorted(nums)[1:-1])//len(nums[2:])
def sum13(nums):
  return sum(nums[i] for i in range(len(nums)) if 13 not in nums[i-1:i+1] and i > 0 or i == 0 and nums[0] != 13)
def sum67(nums):
  return (lambda:sum(nums),lambda:sum(nums[:nums.index(6)]) + sum67(nums[nums.index(7, nums.index(6)) + 1:]))[6 in nums]()
def has22(nums):
  return (2,2) in zip(nums, nums[1:])
print(last2('xaxxaxaxx'))
#Dhruv Anurag 5 2024