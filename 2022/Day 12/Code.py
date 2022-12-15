from pathlib import Path
input=[]
path = Path(__file__).parent / "input.txt"
with path.open() as f:
    for line in f:
        r = line.strip('\n')
        input.append([i for i in r])



# single Node
class Node:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

 
    def __repr__(self):
        return f"Node({self.row}, {self.col}, {self.dist})"


def getValue(n):
    if n == 'S':
        return ord('a')
    if n == 'E':
        return ord('z')
    return ord(n)



# BFS
def startingPoint(grid, part):
    
    sources = []

    erg = []
    # Find startingpoint

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            start = Node(0, 0, 0)
            if part == 1:
                if grid[row][col] == 'S':
                    start.row = row
                    start.col = col
                    sources.append(start)
                    break
            if part ==2:
                if grid[row][col] == 'a':
                    start.row = row
                    start.col = col
                    sources.append(start)

    for node in sources:
        erg.append(minDistance(grid, node))

    shortestPath = 10000000000000000000000
    for element in erg:
        if element < shortestPath and element != -1:
            shortestPath = element
    return shortestPath
    


def minDistance(grid, source):
    # Create second map to check visited
    visited = [[False for _ in range(len(grid[0]))]
               for _ in range(len(grid))]

    queue = []
    queue.append(source)
    visited[source.row][source.col] = True

    while len(queue) != 0:
        source = queue.pop(0)

        #check if destination
        if (grid[source.row][source.col] == 'E'):
            return source.dist
 
        # Check above
        if isValid(source.row, source.col, source.row - 1, source.col, grid, visited):
            queue.append(Node(source.row - 1, source.col, source.dist + 1))
            visited[source.row - 1][source.col] = True
 
        # check down
        if isValid(source.row, source.col, source.row + 1, source.col, grid, visited):
            queue.append(Node(source.row + 1, source.col, source.dist + 1))
            visited[source.row + 1][source.col] = True
 
        # check left
        if isValid(source.row, source.col, source.row, source.col - 1, grid, visited):
            queue.append(Node(source.row, source.col - 1, source.dist + 1))
            visited[source.row][source.col - 1] = True

 
        # check right
        if isValid(source.row, source.col, source.row, source.col + 1, grid, visited):
            queue.append(Node(source.row, source.col + 1, source.dist + 1))
            visited[source.row][source.col + 1] = True

    #return -1 if destination is not found
    return -1


#check if node is Valid
def isValid(cx,cy,x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
        (x < len(grid) and y < len(grid[0])) and
        #cant be smaller, 0 or 1 bigger
            (getValue(grid[x][y]) - getValue(grid[cx][cy]) <= 1) and (visited[x][y] == False)):
        return True 
    return False
 

 
if __name__ == '__main__':
    print("Part 1: " + str(startingPoint(input, 1)))
    print("Part 2: " + str(startingPoint(input, 2)))
