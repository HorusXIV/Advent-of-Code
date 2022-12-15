from pathlib import Path
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n")

screen=[]

for _ in range(6):
    line=[]
    for _ in range(40):
        line.append(" ")
    screen.append(line)




def checkCycle(c,x):
    signalStrength=0
    if (c-20) % 40 == 0:
        signalStrength = c*x
    return signalStrength

def crt(x, pos):
    sprite=[x-1,x,x+1]
    if pos[1] in sprite:
        screen[pos[0]][pos[1]] = "#"
    pos[1] += 1
    if pos[1] > 39:
        pos[0] += 1
        pos[1] = 0

    return pos
    


def part1():
    cycle=0
    x=1
    signalStrengtSum=0

    for line in input:
        if "noop" in line:
            cycle+=1
            signalStrengtSum += checkCycle(cycle,x)
        else:
            cycle+=1
            signalStrengtSum += checkCycle(cycle,x)
            cycle+=1
            signalStrengtSum += checkCycle(cycle,x)
            x += int(line.split(" ")[1])
    return str(signalStrengtSum)

def part2():
    pointer=[0,0]
    x=1
    for line in input:
        if "noop" in line:
            pointer = crt(x, pointer)
        else:
            pointer= crt(x, pointer)
            pointer = crt(x, pointer)
            x += int(line.split(" ")[1])

    for line in screen:
        print(line)


print("Part 1: " + part1())
part2()
