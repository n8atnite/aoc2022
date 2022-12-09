import numpy as np

def findVisibleUnidirectional(arr):
    visible = np.zeros(len(arr), dtype=int)
    tallest = -1
    for i, candidate in enumerate(arr):
        if candidate > tallest:
            visible[i] = 1
            tallest = candidate
    return visible

def findVisibleArray(arr):
    left = findVisibleUnidirectional(arr)
    right = findVisibleUnidirectional(arr[::-1])

    return left + right[::-1]

with open('input8.txt', 'r') as f:
    grid = np.array([[int(char) for char in line.replace('\n', '')] for line in f.readlines() if line.replace('\n', '')])

rows = np.apply_along_axis(findVisibleArray, 1, grid)
cols = np.apply_along_axis(findVisibleArray, 0, grid)

visible = np.bitwise_or(rows, cols)
print(np.count_nonzero(visible))