with open('input1.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines()]
    inventory = [int(entry) if entry else None for entry in entries]

top = []
current = 0
for i in inventory:
    if i is None:
        top.append(current)
        current = 0
    else:
        current += i

print(sum(sorted(top, key=lambda x: x, reverse=True)[:3]))