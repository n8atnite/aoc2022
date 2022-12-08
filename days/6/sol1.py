with open('input6.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines() if line.replace('\n', '')]

unique = []
for i, char in enumerate(entries[0]):
    if char not in unique:
        unique.append(char)
        if len(unique) == 4:
            print(i+1)
            break
    else:
        unique = unique[unique.index(char)+1:] + [char]
