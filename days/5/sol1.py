with open('input5.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines() if line.replace('\n', '')]

# build crate map
crate_entries = [row[i:i+4] for row in entries[:8] for i in range(0, len(row), 4)]
crate_map = [[] for i in range(9)]
for i, entry in enumerate(crate_entries):
    char = [char for char in entry if char.isalpha()]
    if char:
        crate_map[i%9].append(char[0])

# extract controls
control_entries = entries[9:]
steps = [[int(entry.split(' ')[i]) for i in (1,3,5)] for entry in control_entries]

for amount, origin, destination in steps:
    tmp, crate_map[origin-1] = crate_map[origin-1][amount-1::-1], crate_map[origin-1][amount:]
    crate_map[destination-1] = tmp + crate_map[destination-1]

print(''.join([container[0] for container in crate_map]))