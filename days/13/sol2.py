from ast import literal_eval as literal
from functools import cmp_to_key as cmp

# 1 = out of order, -1 = in order, 0 = inconclusive
def compare(left, right):
    ltype, rtype = type(left), type(right)
    if ltype is int:
        if rtype is int:
            return -1 if (left < right) else 1 if (left > right) else 0
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
            return -1 if (len(left) < len(right)) else 1 if (len(left) > len(right)) else 0
    else:
        return ValueError("invalid input")

with open('input13.txt', 'r') as f:
    entries = [literal(line) for line in f.read().splitlines() if line] + [[[2]], [[6]]]

sortedEntries = sorted(entries, key=cmp(compare))

print((sortedEntries.index([[2]])+1)*(sortedEntries.index([[6]])+1))