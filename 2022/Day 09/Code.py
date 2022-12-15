from pathlib import Path
import numpy as np
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n")


    """
            -1, 2	 0, 2	 1, 2	 
    -2, 1	-1, 1	 0, 1	 1, 1	 2, 1 
    -2, 0	-1, 0	 0, 0	 1, 0	 2, 0
    -2- 1	-1,-1	 0,-1	 1,-1	 2,-1
            -1,-2	 0,-2	 1,-2

            -1, 1	 0, 1	 1, 1
    -1, 1	 0, 0	 0, 0	 0, 0	 1, 1
    -1, 0	 0, 0	 0, 0	 0, 0	 1, 0
    -1,-1	 0, 0	 0, 0	 0, 0	 1,-1
            -1,-1	 0,-1	 1,-1
    """

def isadjacent (distance):
    ad = [-1,0,1]
    if distance[0] in ad and distance[1] in ad:
        return True
    return False

def isCorner(distance):
    c = [-2,2]
    if distance[0] in c and distance[1] in c:
        return True
    return False

def stepToO(num):
    return 1 if num>0 else -1


def tailMovement(last, current):
    move = np.array([0,0])
    distance = np.subtract(last, current)
    if isadjacent(distance):
        pass
    elif isCorner(distance):
        move[0] = stepToO(distance[0])
        move[1] = stepToO(distance[1])
    elif distance[0] == 2 or distance[0] == -2:
        move[0] = stepToO(distance[0])
        move[1] = distance[1]
    elif distance[1] == 2 or distance[1] == -2:
        move[0] = distance[0]
        move[1] = stepToO(distance[1])
    
    return move

def solve(x):
    knots = []
    for _ in range(x):
        knots.append([0,0])

    knots = np.array(knots)

    visited = set()

    for line in input:
        command = line.split(" ")[0]
        value=int(line.split(" ")[1])
        for _ in range(value):
            match command:
                case "R":
                    knots[0][0] += 1 
                case "L":
                    knots[0][0] -= 1
                case "U":
                    knots[0][1] += 1
                case "D":
                    knots[0][1] -= 1 
            pos=1
            while pos < x:
                tailMov = tailMovement(knots[pos-1], knots[pos])
                knots[pos] = np.add(knots[pos], tailMov)
                if pos == x-1:
                    visited.add((knots[pos][0],knots[pos][1]))
                pos+=1
    return str(len(visited))

print("Part 1: "+ solve(2))
print("Part 2; "+ solve(10))



