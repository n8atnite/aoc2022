def soln(entries):
    X = 1
    cycles = 0
    signals = []
    signalStrength = lambda x,c: x*c
    for instruction in enumerate(entries):
        if instruction[0] == 'addx':
            val = int(instruction[1])
            cycles += 2
            if (cycles%40) == 20:
                signals.append(signalStrength(X, cycles))
            elif (cycles%40) == 21:
                signals.append(signalStrength(X, cycles-1))
            X += val
        else: # noop
            cycles += 1
            if (cycles%40) == 20:
                signals.append(signalStrength(X, cycles))

    return signals

with open('input10.txt', 'r') as f:
    entries = [line.split(' ') for line in f.read().splitlines()]

result = soln(entries)
print(sum(result))
