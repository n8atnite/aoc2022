def is_contained(a, b):
    if a[0] >= b[0]:
        if a[1] <= b[1]:
            return True
    return False

with open('input4.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines()]

contained = 0
for entry in entries:
    check = False
    assignments = [[int(i) for i in pair.split('-')] for pair in entry.split(',')]
    if is_contained(assignments[0], assignments[1]):
        contained += 1
    elif is_contained(assignments[1], assignments[0]):
        contained += 1

print(contained)