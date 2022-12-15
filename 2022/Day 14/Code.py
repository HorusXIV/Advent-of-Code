from pathlib import Path
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    input = f.read().split("\n")