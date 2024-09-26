csp_table = {0: {1, 19, 10}, 1: {0, 2, 8}, 2: {1, 3, 6}, 3: {2, 19, 4}, 4: {5, 3, 17}, 5: {4, 6, 15}, 6: {2, 7, 5}, 7 : {6, 8, 14}, 8: {1, 7, 9}, 9: {10, 8, 13}, 10 : {9, 11, 0},
   11 : {10, 12, 18}, 12: {11, 13, 16}, 13: {9, 12, 14}, 14: {15, 13, 7}, 15: {5, 14, 16}, 16: {15, 12, 17}, 17: {16, 18, 4}, 18: {11, 17, 19}, 19: {0, 3, 18}}
longestset, templongestset = {i : {i} for i in range(20)}, {i : {i} for i in range(20)}
original = True
for a in range(20):
    for d in range(20):
        for b in range(d, 20):
            if b not in csp_table[a]:
                    for c in templongestset[a]:
                        if b in csp_table[c]: original = False
                    if original == True: templongestset[a].add(b)
            original = True
        if len(templongestset[a]) > len(longestset[a]): longestset[a], templongestset[a] = templongestset[a], set()
print(max(longestset.values(), key = len))