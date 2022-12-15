from pathlib import Path
path = Path(__file__).parent / "AoCinput.txt"
with path.open() as f:
    AoCinput = [x for x in f.read().split("\n")]



def mostcommmonN(i, AoCinput):
    ones = 0
    zeros = 0
    for Number in AoCinput:
        if Number[i] == "0":
            zeros += 1
        elif Number[i] == "1":
            ones += 1
    if zeros > ones:
        return(0)
    else:
        return(1)

def part1(AoCinput):
    i = 0
    gamma = ""
    epsilon = "" 
    while i <= len(AoCinput[1])-1:
        mcN = mostcommmonN(i, AoCinput)
        if mcN == 0:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
        i += 1

    print(int(gamma, 2)*int(epsilon, 2))


def getValues(AoCinput, grabco2):
    co2 = []
    testsequence = ""
    i = 0
    erglist=[]
    while i <= len(AoCinput[1])-1:
        erglist = []
        #if the Value of CO2 is searched, the most common number is inverted to deliver the least frequent number. Else the returnvalue of mostcommonN will be used
        if grabco2:
            testbit = 1 - mostcommmonN(i, AoCinput)
        else:
            testbit = mostcommmonN(i, AoCinput)
        testsequence += str(testbit)
        for Number in AoCinput:
            if Number.startswith(testsequence):
                erglist.append(Number)
        AoCinput = erglist
        i+=1
        if len(erglist) == 1:
            break
    return(int(erglist[0], 2))

def part2():
   print(getValues(AoCinput, False) * getValues(AoCinput, True)) 

part1(AoCinput)
part2()