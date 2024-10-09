from pathlib import Path
path = Path(__file__).parent / "AoCinput.txt"
with path.open() as f:
    input = [x for x in f.read().split("\n")]

def part1(AoCinput):
    larger = 0
    lastm = 1000000
    prelastm = 100000


    for measurement in AoCinput:
        measurement = int(measurement)
        if measurement > lastm:
            larger += 1
        lastm = measurement
    print(larger)

def part2(AoCinput):
    i = 2
    larger = 0
    lasterg = 100000000000000000000000000000000000000000000000000000000


    while i <= len(AoCinput)-1:
        erg = int(AoCinput[i-2]) + int(AoCinput[i-1]) + int(AoCinput[i])  
        if erg > lasterg:
            larger += 1
        lasterg = erg
        i += 1
    print(larger)


part1(input)
part2(input)