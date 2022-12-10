DIRECTIONS = {
    'U': (1,0),
    'D': (-1,0),
    'R': (0,1),
    'L': (0,-1)
}

# adjust tail position based on new head position
CORRECTIONS = { 
    'U': (-1,0),
    'D': (1,0),
    'R': (0,-1),
    'L': (0,1),
    'UR': (-1,-1),
    'UL': (-1,1),
    'DR': (1,-1),
    'DL': (1,1)
}

calculatePos = lambda p, d : tuple((sum(i) for i in zip(p, d)))
def calculateFar(x, y):
    diffx = x[0]-y[0]
    diffy = x[1]-y[1]
    res = ''
    if abs(diffx) > 1:
        res += 'U' if diffx > 0 else 'D'
    if abs(diffy) > 1:
        res += 'R' if diffy > 0 else 'L'
    return res

with open('input9.txt', 'r') as f:
    entries = [line.split(' ') for line in f.read().splitlines()]

rope = [(0,0) for _ in range(10)]
visited = {(0,0),}
for direction, amount in entries:
    for i in range(int(amount)):
        rope[0] = calculatePos(rope[0], DIRECTIONS[direction])
        for j in range(1, len(rope)):
            farDirection = calculateFar(rope[j-1], rope[j])
            if farDirection:
                rope[j] = calculatePos(rope[j-1], CORRECTIONS[farDirection])
                if j == 9:
                    visited.add(rope[j])

print(len(visited))