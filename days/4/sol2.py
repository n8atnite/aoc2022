def is_overlapped(a, b):
    if a[0] <= b[1]:
        if a[1] >= b[0]:
            return True
    return False

with open('input4.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines()]

overlapped = 0
for entry in entries:
    check = False
    assignments = [[int(i) for i in pair.split('-')] for pair in entry.split(',')]
    if is_overlapped(assignments[0], assignments[1]):
        overlapped += 1

print(overlapped)