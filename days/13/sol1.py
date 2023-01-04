from ast import literal_eval as literal

# -1 = out of order, 1 = in order, 0 = inconclusive
def compare(left, right):
    ltype, rtype = type(left), type(right)
    if ltype is int:
        if rtype is int:
            return 1 if (left < right) else -1 if (left > right) else 0
        elif rtype is list:
            return compare([left], right)
    elif ltype is list:
        if rtype is int:
            return compare(left, [right])
        elif rtype is list:
            for l,r in list(zip(left, right)):
                result = compare(l,r)
                if result:
                    return result
            return 1 if (len(left) < len(right)) else -1 if (len(left) > len(right)) else 0
    else:
        return ValueError("invalid input")

with open('input13.txt', 'r') as f:
    entries = [literal(line) for line in f.read().splitlines() if line]

correctIndexSum = 0
for i, (left, right) in enumerate(list(zip(entries[::2], entries[1::2]))):
    a = compare(left, right)
    if a > 0:
        correctIndexSum += (i+1)

print(correctIndexSum)