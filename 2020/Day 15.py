def get2020Element(list:list):
    while len(list) < 2020:
        distance = 1
        if list[-1] not in list[:-1]:
            list.append(0)
        else: 
            for element in reversed(list[:-1]):
                if element != list[-1]:
                    distance += 1
                else:
                    list.append(distance)
                    break
    print(list[-1])

def getXElementImproved(lastelement:int, input:list):
    turn = len(input)
    mem = {input[i]: i + 1 for i in range(len(input) - 1)}
    last_spoken = input[-1]

    while turn < lastelement:
        if last_spoken in mem:
            speak = turn - mem[last_spoken]
        else:
            speak = 0

        mem[last_spoken] = turn
        last_spoken = speak
        turn += 1
    
    print(speak)
    
get2020Element([6,3,15,13,1,0])
getXElementImproved(30000000,[6,3,15,13,1,0])