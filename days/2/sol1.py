RULES = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

with open('input2.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines()]

count = 0
for entry in entries:
    count += RULES[entry]

print(count)