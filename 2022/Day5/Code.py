from pathlib import Path
import copy as cp
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n\n")


"""stacks = [
    [],
    [],
    [],
    [],
    [] 
]

def prepareStacks(line):
        print(line)



for line in input[0]:
    print(line)
    if ("[" in line):
        print(line.rstrip("\n").replace("    ", " ").split(" "))
        prepareStacks(line.rstrip("\n").replace("    ", " ").split(" "))
    print(stacks)


"""
cargo =[
    ["C", "Z", "N", "B", "M", "W", "Q", "V"],
    ["H", "Z", "R", "W", "C", "B"],
    ["F", "Q", "R", "J"],
    ["Z", "S", "W", "H", "F", "N", "M", "T"],
    ["G", "F", "W", "L", "N", "Q", "P"],
    ["L", "P", "W"],
    ["V", "B", "D", "R", "G", "C", "Q", "J"],
    ["Z", "Q", "N", "B", "W"],
    ["H", "L", "F", "C", "G", "T", "J"]
]

def solve(version):
    erg=""
    wk = cp.deepcopy(cargo)
    for line in input[1].split("\n"):
        amount = int(line.split(",")[0])
        stableFrom = int(line.split(",")[1])-1
        stapleTo = int(line.split(",")[2])-1

        if version == 9000:
            for i in range(0,amount):
                create = wk[stableFrom].pop()
                wk[stapleTo].append(create)
        else:
            load = wk[stableFrom][-amount:]
            wk[stableFrom] = wk[stableFrom][:len(wk[stableFrom]) - amount]
            wk[stapleTo].extend(load)     

    for line in wk:
        erg+=line.pop()

    return erg


print("part 1: " + solve(9000))
print("part 1: " + solve(9001))