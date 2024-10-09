import itertools
from pathlib import Path
path = Path(__file__).parent / "AoCinput.txt"
with path.open() as f:
    AoCinput = [x for x in f.read().split("\n\n")]

def winCheck(Board):
    i=0
    verticalCheck=[]
    while i < len(Board[0]):
            column = []
            for line in Board:
                column.append(line[i])
            i+=1
            verticalCheck.append((column))

    return (checkLines(Board) or checkLines(verticalCheck))

def calcSum(Board):
    sum=0
    for line in Board:
        for value in line:
            if value != "X":
                sum+=int(value)
    return sum

def checkLines(Board):
    for line in Board:
        win=False
        for value in line:
            if value != "X":
                win=False
                break
            else:
                win=True
        if win:
            return True
    return False 

        

def part1(Data,part):
    numbers= Data[0]
    Boards = []
    sum=0
    for board in Data[1:]:
        newBoard=[]
        for line in board.split("\n"):
            newBoard.append(line.strip().split(" "))
        Boards.append(newBoard)

    for number in numbers.split(","):
        won=False
        for x, Board in enumerate(Boards):
            for y, line in enumerate(Board):
                for z, value in enumerate(line):
                    if value == number:
                        Boards[x][y][z] = "X"
            


        for Board in Boards:
            if winCheck(Board):
                if part==1:
                    sum = calcSum(Board)
                    return sum*int(number)
                if part == 2:
                    if len(Boards) > 1:
                        Boards.remove(Board)
                    else:
                        sum = calcSum(Boards[0])
                        return sum*int(number) 
                   
        
print(part1(AoCinput,1))
print(part1(AoCinput,2))