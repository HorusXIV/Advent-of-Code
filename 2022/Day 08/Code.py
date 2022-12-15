from pathlib import Path
import copy as cp
import random as rnd
import numpy as np

input=[]
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    for line in f.read().split("\n"):
        input.append(list(line))

def visible(array):
    trow=[]
    for i, tree in enumerate(array):
        if i == 0:
            trow.append(True)
        elif int(tree) > int(array[i-1]):
            trow.append(True)
        else:
            trow.append(False)
            array[i] = array[i-1]
    return(trow)


def checkLine(array):
    rev = visible(list(reversed(array)))
    rev.reverse()
    array = visible(array)
    line = np.logical_or(array, rev)
    return line

def part1():
    topdownmap = []
    i=0
    while i < len(input):
        column = []
        for line in input:
            column.append(line[i])
        i+=1
        topdownmap.append(checkLine(column))

    topdownmap = np.array(topdownmap).transpose()

    leftrightmap = []
    for line in input:
        leftrightmap.append(checkLine(line))

    leftrightmap = np.array(leftrightmap)


    return str(np.count_nonzero((np.logical_or(topdownmap, leftrightmap))==True))


def getScore(array, x,y):
    canSee = True
    score = 0
    for tree in array:
        score+=1
        if tree >= input[x][y]:
            canSee = False
        if not canSee:
            break
    return score

def part2():
    highestScore = 0
    transposedMap = []
    i=0
    while i < len(input):
        column = []
        for line in input:
            column.append(line[i])
        i+=1
        transposedMap.append((column))


    x=0
    while x < len(input):
        y= 0
        while y < len(input[0]):
            oberhalb = list(reversed(transposedMap[y][:x]))
            unterhalb = transposedMap[y][x+1:]
            vorher = list(reversed(input[x][:y]))
            nacher = input[x][y+1:]
            treeScore = getScore(oberhalb, x, y)*getScore(unterhalb, x, y)*getScore(vorher, x, y)*getScore(nacher, x, y)
            if treeScore>highestScore:
                highestScore=treeScore
            y+=1
        x+=1

    return str(highestScore)

   


print("Part 1: " + part1())
print("Part 2: " + part2())