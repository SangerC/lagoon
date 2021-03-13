import sys

memorySize = 324

inc = set()
dec = set()
inp = set()
out = set()
memory = [0]*memorySize

def tick():
    for i in inc:
        memory[i]+=1
    for i in dec:
        memory[i]-=1
    for i in out:
        print(chr(memory[i]), end='')
    if len(inp)>0:
        value = input()
        for i in inp:
            memory[i] = ord(value)
    print(memory)

def toggle(index, pool):
    if index in pool:
        pool.remove(index)
    else:
        pool.add(index)

def getNumeric(index, lagoon):
    startIndex = index[0]
    while index[0] < len(lagoon) and lagoon[index[0]].isnumeric():
        index[0]+=1
    return int(lagoon[startIndex:index[0]]) 

def operate(address, operator):
    if operator == '+':
        toggle(address, inc)
    elif operator == '-':
        toggle(address, dec)
    elif operator == 'i':
        toggle(address, inp)
    elif operator == 'o':
        toggle(address, out)

def followPointer(address, pointers):
    print(address)
    print(pointers)
    if pointers == 2:
        return memory[address]
    return followPointer(memory[address], pointers-1)

def findPointers(index, lagoon):
    startIndex = index[0]
    while lagoon[index[0]] == '>':
        index[0]+=1
    return followPointer(getNumeric(index, lagoon), index[0]-startIndex)

def getGuard(lagoon):
    options = lagoon.split(',')
    checks = []

    for o in options:
        index = [0]
        if o[index[0]] == '!':
            index[0]+=1
        if o[index[0]] != '>':
            address = getNumeric(index, o)
            if(o[0]=='!'):
                checks.append(lambda : memory[address]!=0)
            else:
                checks.append(lambda : memory[address]==0)
        else:
            if(o[0]=='!'):
                checks.append(lambda : memory[findPointers(index,o)]!=0)
            else:
                checks.append(lambda : memory[findPointers(index,o)]==0)

    def guard():
        for i in checks:
            if i():
                return True
        return False

    return guard


def interpret(lagoon):
    index = [0]
    
    while index[0] < len(lagoon):
        if lagoon[index[0]]==';':
            tick()
        elif lagoon[index[0]].isnumeric(): 
            address = getNumeric(index, lagoon)
            operate(address, lagoon[index[0]])
        elif lagoon[index[0]] == '>':
            address = findPointers(index, lagoon)  
            operate(address, lagoon[index[0]])
        elif lagoon[index[0]] == '[':
            startIndex = index[0]+1
            while lagoon[index[0]] != '|':
                index[0]+=1
            checkGuard = getGuard(lagoon[startIndex:index[0]])
            startIndex = index[0]+1
            while lagoon[index[0]] != ']':
                index[0]+=1
            while(checkGuard()):
                interpret(lagoon[startIndex:index[0]])
        index[0]+=1

def getInput():
    value = ord(input())
    for i in inp:
        memory[i] = value

def main():
    file = open(sys.argv[1])
    text = file.read()
    
    interpret(text)

main()






