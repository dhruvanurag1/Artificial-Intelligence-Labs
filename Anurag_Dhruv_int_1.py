count = 0
def solve(count, a):
    li, dic, hours, minutes, numbers = a.split(), {"R" : 0, "G" : 0, "B" : 0, "W": 0}, 0, 0, [1,1,2,3,5]
    for a in range(len(li)): dic[li[a]] += numbers[a]
    hours, minutes = dic["R"] + dic["B"], (dic["G"] + dic["B"]) * 5
    if minutes == 60: hours, minutes = hours + 1, minutes - 60
    if hours > 12: hours = hours % 12
    return str(count) + '. ' + (str(hours) if len(str(hours)) == 2 else '0' + str(hours)) + ':' + (str(minutes) if len(str(minutes)) == 2 else '0' + str(minutes))
with open('test.txt', "r") as file: 
    for line in file: print(solve((count:=count+1), line))