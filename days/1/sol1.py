with open('input1.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines()]
    inventory = [int(entry) if entry else None for entry in entries]

top = 0
current = 0
for i in inventory:
    if i is None:
        if current > top:
            top = current
        current = 0
    else:
        current += i

print(top)