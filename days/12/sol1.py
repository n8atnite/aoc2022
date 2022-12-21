import heapq as pq
import numpy as np

def neighborsOf(index): 
    return [
        (index[0] - 1, index[1]), 
        (index[0] + 1, index[1]), 
        (index[0], index[1] - 1), 
        (index[0], index[1] + 1)
    ]

def findDistance(heightmap, startIndex, endIndex): 
    nextNodes = []
    currentIndex = startIndex
    visited = {startIndex} 
    distance = 0
    
    while startIndex != endIndex:
        for neighborIndex in neighborsOf(startIndex):
            try:
                diff = heightmap[startIndex] - heightmap[neighborIndex]
            except IndexError:
                continue
            if neighborIndex not in visited and diff >= -1:
                visited.add(neighborIndex)
                pq.heappush(nextNodes, (distance+1, neighborIndex))
        if not nextNodes:
            return np.inf
        distance, startIndex = pq.heappop(nextNodes)

    return distance

with open("input12.txt", "r") as f: 
    lines = f.read().splitlines()
    heightmap = np.zeros((len(lines), len(lines[0])))
    for i, line in enumerate(lines): 
        for j, char in enumerate(line): 
            if char == 'S':
                startIndex = (i,j)
                char = 'a'
            elif char == 'E': 
                endIndex = (i,j)
                char = 'z'
            heightmap[i][j] = ord(char)

print(findDistance(heightmap, startIndex, endIndex))