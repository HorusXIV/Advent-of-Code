from pathlib import Path
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n\n")

list = ["","","",""]
str = "list"

print(eval(str))


""" for set in input:
    pair = set.split("\n")
    print(pair)
    print("--")
     """