arrayy = [[-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 1, -1, -1, -1, -1, -1, 1, -1], [-1, -1, 1, -1, -1, -1, 1, -1, -1], [-1, -1, -1, 1, -1, 1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, -1, -1, -1]]
arrays = arrayy + arrayy[:-1][::-1]
def matrixdot(one, two):
    return sum(one[i][j] * two[i][j] for i in range(len(one[0])) for j in range(len(one)))
def test_slice(m):
    width = len(m[0])
    height = len(m)
    print(height - 2, width - 2)
    slices = []
    for i in range(0, height - 2):
        for j in range(0, width - 2):
            slices.append([[m[a][b] for b in range(j, j + 3)] for a in range(i, i + 3)])
    slice_combined = []
    for i in range(0, len(slices)-3, 3):
        slice_combined.append(slices[i:i+3])
    return slices
print(test_slice(arrays))
filter1 = [[-1,-1,1], [-1, 1, -1], [1, -1, -1]]
lists=[]
for a in test_slice(arrays):
    lists.append(matrixdot(a, filter1))
print(lists)
print(len(lists))
