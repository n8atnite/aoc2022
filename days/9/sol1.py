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
    'L': (0,1)
}

calculatePos = lambda p, d : tuple((sum(i) for i in zip(p, d)))
isFar = lambda x, y: True if (abs(x[0]-y[0]) > 1) or (abs(x[1]-y[1]) > 1) else False

with open('input9.txt', 'r') as f:
    entries = [line.split(' ') for line in f.read().splitlines()]

hpos = tpos = (0,0)
visited = {(0,0),}
for direction, amount in entries:
    for i in range(int(amount)):
        hpos = calculatePos(hpos, DIRECTIONS[direction])
        if isFar(hpos, tpos):
            tpos = calculatePos(hpos, CORRECTIONS[direction])
            visited.add(tpos)

print(len(visited))