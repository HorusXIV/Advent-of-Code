from pathlib import Path
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n")

#Part 1
sum = 0
sumlist = []

for entry in input:
    if entry != '':
        sum += int(entry)
    elif entry == '':
        sumlist.append(sum)
        sum = 0

print("Solution part 1: " + str(max(sumlist)))

#Part2
sumlist.sort()
erg=0

#erg = sum(sumlist[-3:])
for value in sumlist[-3:]:
    erg += int(value)

print("Solution part 2: "+ str(erg))