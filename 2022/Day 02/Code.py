from pathlib import Path
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    inputList = list(map(lambda x: x.split(" "), f.read().split("\n")))

mapper = {'X': '1', 'Y':'2', 'Z':'3', 'A': '1', 'B':'2', 'C':'3'}

def part1(input):
    score = 0
    for game in input:
        opponentChoice = int(mapper[game[0]])
        myChoice = int(mapper[game[1]]) 
        score += myChoice
        if myChoice == opponentChoice:
            score += 3
        elif myChoice - 1 == opponentChoice or (myChoice == 1 and opponentChoice == 3):
            score += 6
    print("Part 1: " + str(score))

def part2(input):
    score = 0
    for game in input:
        opponentChoice = int(mapper[game[0]])
        action = int(mapper[game[1]]) 
        score += 3 if action == 2 else 6 if action == 3 else 0

        if action == 2:
            score += opponentChoice
        elif opponentChoice == 2:
            score += action
        elif opponentChoice != action:
            score += 2
        elif action == 1:
            score += 3
        elif action == 3:
            score +=  1

    print("Part 2: " + str(score))


part1(inputList)
part2(inputList)