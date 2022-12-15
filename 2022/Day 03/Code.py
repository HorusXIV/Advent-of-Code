import string
from pathlib import Path
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n")

def calcPrio(key):
    priority = (string.ascii_lowercase.index(key.lower())) + 1 
    if key.isupper():
        priority += 26
    return priority



#TODO: sliding Window





def part1():
    score = 0
    for line in input:
        firstCompartment = line[:len(line)//2]
        secondCompartment = line[len(line)//2:]

        type = ""

        for letter in firstCompartment:
            if letter in secondCompartment:
                type = letter
        
        priority = calcPrio(type)

        score += priority
    print("Part 1: " + str(score))


def part2():
    score=0
    i=1
    badge=""
    while i<=len(input):
        for letter in input[i]:
            if letter in input[i-1] and letter in input[i+1]:
                badge = letter
        score += calcPrio(badge)
        i+=3
    print("Part 2: " + str(score))

part1()
part2()
