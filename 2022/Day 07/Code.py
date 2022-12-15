from pathlib import Path
from dataclasses import dataclass

path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n")

directorys = {}
i=0
node="-"




"""
@dataclass
class Node:
    name: str
    parent: Node
    children: list
    files: dict

    def __init__(self, name: str, parent:Node) -> None:
        pass
"""

"""
for line in input:
    if "ls" == line.split(" ")[0]:
        
        node = line.split(" ")[1]
        print(node)

    i+=1
"""



"""
for line in input:
    kind = line.split(" ")[0]
    if "$" == kind:
        match line.split(" ")[1]:
            case "cd":
                if line.split(" ")[2] == "..":
                    print("back")
                else:
                    print("move into: " + line.split(" ")[2])
            case "ls":
                x=1
                sum=0
                while True:
                    if (i+x) >= len(input):
                        break  
                    if input[i+x][0] != "$":
                        if input[i+x].split(" ")[0] == "dir":
                            dirname = input[i+x].split(" ")[1]
                            print(dirname + " contains: ")
                        else:
                            print(input[i+x].split(" ")[0])
                        x+=1
                    else:
                        break
            case _:
                print("unvalid input")
    i+=1
    """