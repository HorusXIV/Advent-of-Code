from pathlib import Path
path = Path(__file__).parent / "AoCinput.txt"
with path.open() as f:
    AoCinput = [x for x in f.read().split("\n")]

def part1():
    x = 0
    depth = 0

    for input in AoCinput:
        direction = input.split(" ")[0]
        distance = int(input.split(" ")[1])
        if direction == "forward":
            x += distance   
        elif direction == "up":
            depth -= distance
        elif direction == "down":
            depth += distance
            
    print(x*depth)


def part2():
    x = 0
    depth = 0
    aim = 0

    for input in AoCinput:
        direction = input.split(" ")[0]
        number = int(input.split(" ")[1])
        if direction == "forward":
            x += number
            if aim >= 0:
                depth += aim * number
        elif direction == "up":
            aim -= number
        elif direction == "down":
            aim += number
            
    print(x*depth)



part1()
part2()