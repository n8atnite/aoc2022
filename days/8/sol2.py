import numpy as np

def findScoreUnidirectional(arr):
    score = np.ones(len(arr), dtype=int)
    for i, tree in enumerate(arr[:-1]):
        count = 1
        for neighbor in arr[i+1:-1]:
            if tree <= neighbor:
                break
            count += 1
        score[i] = count if count else 1
    return score

def findScoreArray(arr):
    left = findScoreUnidirectional(arr)
    right = findScoreUnidirectional(arr[::-1])

    return left * right[::-1]

with open('input8.txt', 'r') as f:
    grid = np.array([[int(char) for char in line.replace('\n', '')] for line in f.readlines() if line.replace('\n', '')])

rows = np.apply_along_axis(findScoreArray, 1, grid)
cols = np.apply_along_axis(findScoreArray, 0, grid)

scores = rows * cols
print(np.max(scores))