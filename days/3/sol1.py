set_priorities = lambda r,a: {chr(code): i + a for i, code in enumerate(r)}

PRIORITIES = {}
PRIORITIES.update(set_priorities(range(97, 123), 1)) # lowercase
PRIORITIES.update(set_priorities(range(65, 91), 27)) # uppercase

with open('input3.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines()]

priority_sum = 0
for sack in entries:
    c1, c2 = set(sack[:len(sack)//2]), set(sack[len(sack)//2:])
    (same,) = c1.intersection(c2)
    priority_sum += PRIORITIES[same[0]]

print(str(priority_sum))