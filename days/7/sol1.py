class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Folder:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.children = {}
        self.files = []

    def __str__(self):
        return self.getPath()

    def getPath(self, current=''):
        current = '/%s' % (self.name,) + current if self.name != '/' else current
        if (not current) and (not self.parent): # base path edge case
            return '/'
        return self.parent.getPath(current=current) if self.parent else current

    def addChild(self, entry):
        self.children.append(entry)

    def addFile(self, entry):
        self.files.append(entry)

    def getSize(self):
        if len(self.children.keys()) > 0:
            return sum([f.size for f in self.files]) + sum([d.getSize() for d in self.children.values()])
        else:
            return sum([f.size for f in self.files])

def getAllSizes(folder, sizes):
    sizes[str(folder)] = folder.getSize()
    for child in folder.children.values():
        getAllSizes(child, sizes)

with open('input7.txt', 'r') as f:
    entries = [line.replace('\n', '') for line in f.readlines() if line.replace('\n', '')]

cwd = Folder('/', None)
fs = [cwd]
for entry in entries:
    line = entry.split(' ')
    if line[0] == '$':
        if line[1] == 'cd': # only check cd; ls is implicit
            if line[2] != cwd.name:
                if line[2] == '..':
                    cwd = cwd.parent
                else:
                    cwd = cwd.children[line[2]]
    elif line[0] == 'dir':
        cwd.children[line[1]] = Folder(line[1], cwd)
    else: # file
        cwd.files.append(File(line[1], int(line[0])))

allSizes = {}
getAllSizes(fs[0], allSizes)
print(sum([size for size in allSizes.values() if size <= 100000]))