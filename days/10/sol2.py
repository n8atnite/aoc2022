from sys import stdout

def rasterize(x, cycle):
    stdout.write('#' if abs(x-(cycle-1)) <= 1 else '.')

def soln(entries):
    X = 1
    pending = 0
    for cycle in range(1, 241):
        if not pending:
            instruction = entries.pop(0)
            if instruction[0] == 'addx':
                pending = int(instruction[1])
            rasterize(X, cycle)
        else:
            rasterize(X, cycle)
            X += pending
            pending = 0
        if cycle%40 == 0:
            X += 40
            stdout.write('\n')

with open('input10.txt', 'r') as f:
    entries = [line.split(' ') for line in f.read().splitlines()]

soln(entries)