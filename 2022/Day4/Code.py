from pathlib import Path
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n")

def createFullCode(start, end):
    erg = []
    while start <= end:
        erg.append(start)
        start += 1
    return erg


#TODO: Ask Orlando regarding complexity

def part1():
    counter=0
    for line in input:
        line = line.split(",")
        if ((int(line[0].split("-")[0]) <= int(line[1].split("-")[0])) and (int(line[0].split("-")[1]) >= int(line[1].split("-")[1])) or (int(line[0].split("-")[0]) >= int(line[1].split("-")[0])) and (int(line[0].split("-")[1]) <= int(line[1].split("-")[1]))):
            counter+=1
    print("Part 1: " + str(counter))


def part2():
    counter=0
    elf1 = ""
    elf2 = ""
    for line in input:
        line = line.split(",")
        elf1 = createFullCode(int(line[0].split("-")[0]), int(line[0].split("-")[1]))
        elf2 = createFullCode(int(line[1].split("-")[0]), int(line[1].split("-")[1]))
        overlap = False
        for element in elf1:
            if element in elf2:
                overlap = True
        if overlap:
            counter += 1
    print("Part 2: " + str(counter))
  

part1()
part2()