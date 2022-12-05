from more_itertools import grouper

set_priorities = lambda r,a: {chr(code): i + a for i, code in enumerate(r)}

PRIORITIES = {}
PRIORITIES.update(set_priorities(range(97, 123), 1)) # lowercase
PRIORITIES.update(set_priorities(range(65, 91), 27)) # uppercase

with open('input3.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines()]

priority_sum = 0
grouped_entries = list(grouper(entries, 3))
for group in grouped_entries:
    sacks = [set(sack) for sack in group]
    (same,) = set.intersection(*sacks)
    priority_sum += PRIORITIES[same[0]]

print(str(priority_sum))