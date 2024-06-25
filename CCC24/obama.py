# doesnt work
rows = int(input())
columns = int(input())

grid = []

for y in range(rows):
    grid.append(list(input()))

for i in range(len(grid)):
    print(grid[i])

starty = int(input())
startx = int(input())

dol = 0

def DFS(x, y, grid):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return
    pos = grid[y][x]
    match pos:
        case '*':
            return
        case 'L':
            dol += 10
        case 'M':
            dol += 5
        case 'S':
            dol += 1
    # left
    DFS(x-1, y, grid)
    DFS(x+1, y, grid)
    DFS(x, y-1, grid)
    DFS(x, y+1, grid)

DFS()