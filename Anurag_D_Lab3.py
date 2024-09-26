def generate_adjacents(current, word_list):
    adj_list = set()
    for i in range(6):
        for j in list("abcdefghijklmnopqrstuvwxyz"):
            if current[:i] + j + current[i+1:] in word_list and current[:i] + j + current[i+1:] != current:
                adj_list.add(current[:i] + j + current[i+1:])
    return adj_list

def display_path_BFS(n, explored):
    l = []
    while explored[n] != "s":
        l.append(n)
        n = explored[n]
    l.append(list(explored.keys())[list(explored.values()).index("s")])
    print(l[::-1])
    print("\n\nshortest path length: " + str(len(l)))
    return ""

def display_path_DLS(n, explored):
    l = []
    while explored[n] != "s":
        l.append(n)
        n = explored[n]
    l.append(list(explored.keys())[list(explored.values()).index("s")])
    print(l[::-1])
    print("\n\nSteps within limit: " + str(len(l)))
    return ""

def BFS(start, end, word_dict):
   explored = {start:"s"}
   q = []
   q.append(start)
   while(len(q) > 0):
       if(len(q) == 0):
        return(["no solution"],0)
       s = q.pop(0)
       if(s == end) :
           return display_path_BFS(s, explored)
       for a in generate_adjacents(s,word_dict):
           if a not in explored:
               q.append(a)
               explored[a] = s

def recur(start, end, word_dict, explored, limit):
    if start == end:
        return display_path_DLS(end, explored)
    elif limit == 0:
        return "No Solution"
    else:
        for a in generate_adjacents(start, word_dict):
            if a not in explored:
                explored[a] = start
                result = recur(a, end, word_dict, explored, limit-1)
                if result == True:
                   return display_path_DLS(start, explored)

def DLS(start, end, word_dict, limit):
    explored = {start:"s"}
    return recur(start, end, word_dict, explored, limit-1)

def read_file():
    a_file = open("words.txt", "r")
    li = []
    for line in a_file:
        li.append(line[:-1])
    return li

def main():
    word1 = input("Type the starting word: ")
    word2 = input("Type the goal word: ")
    l = read_file()
    print(BFS(word1, word2, l))
    limit = input("Type the limit (1 - 20): ")
    word1 = input("Type the starting word: ")
    word2 = input("Type the goal word: ")
    print("Path: ", end = " ")
    DLS(word1, word2, l, int(limit))
    print("Shortest path: ", end = " ")
    print(BFS(word1, word2, l))
    
if __name__ == '__main__':
    main()