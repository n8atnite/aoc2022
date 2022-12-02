RULES = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

with open('input2.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines()]

count = 0
for entry in entries:
    count += RULES[entry]

print(count)