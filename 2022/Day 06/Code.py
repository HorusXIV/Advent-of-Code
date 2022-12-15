from pathlib import Path
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read()

def solution(dC):
    iterator=0
    while iterator <= len(input)-1:
        breakLoop=True
        fourLetters = input[iterator:iterator+dC]
        for letter in fourLetters:
            if fourLetters.count(letter) > 1:
                breakLoop = False
        if breakLoop:
            break
        iterator+=1
    return str(iterator+dC)


print("part 1: " + solution(4))
print("part 2: " + solution(14))











