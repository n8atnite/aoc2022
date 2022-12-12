import re
import operator as ops
from collections import OrderedDict as odict

OPS = {
    '+': ops.add,
    '-': ops.sub,
    '*': ops.mul,
    '/': ops.floordiv
}

class Monkey:
    def __init__(self, startingItems, funcArgs, testValue, truePartner, falsePartner):
        self.inventory = startingItems
        
        self.operation = lambda x: funcArgs[0](x, (x if funcArgs[1] == 'old' else int(funcArgs[1])))
        self.test = testValue
        self.truePartner = truePartner
        self.falsePartner = falsePartner
        self.activity = 0

    def inspectItem(self):
        throwable = self.operation(self.inventory.pop(0))
        if throwable%self.test == 0:
            partner = self.truePartner
        else:
            partner = self.falsePartner

        self.activity += 1
        return partner, throwable

with open('input11.txt', 'r') as f:
    entries = [[word for word in line.split(' ') if word] for line in f.read().splitlines() if line]

# populate fields
monkeys = odict()
params = []
reducer = 1
for i, entry in enumerate(entries):
    index = i%6
    if index == 0:
        params.append(int(entry[1][0]))
    elif index == 1:
        params.append([int(re.sub("[^0-9]", "", num)) for num in entry[2:]])
    elif index == 2:
        params.append((OPS[entry[4]], entry[5]))
    elif index == 3:
        params.append(int(entry[3]))
        reducer *= int(entry[3])
    elif index == 4:
        params.append(int(entry[5]))
    elif index == 5:
        params.append(int(entry[5]))
        monkeys[params[0]] = Monkey(*params[1:])
        params = []

for round in range(10000):
    for monkey in monkeys.values():
        while monkey.inventory:
            res = monkey.inspectItem()
            monkeys[res[0]].inventory.append(res[1]%reducer)

print(ops.mul(*sorted([m.activity for m in monkeys.values()], reverse=True)[:2]))