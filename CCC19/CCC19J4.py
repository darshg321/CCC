flip = input()

grid = [[1, 2],
        [3, 4]]

def horflip(grid):
    newgrid = [[],
               []]
    newgrid[0].append(grid[1][0])
    newgrid[0].append(grid[1][1])
    newgrid[1].append(grid[0][0])
    newgrid[1].append(grid[0][1])
    return newgrid

def verflip(grid):
    newgrid = [[],
               []]
    newgrid[0].append(grid[0][1])
    newgrid[0].append(grid[0][0])
    newgrid[1].append(grid[1][1])
    newgrid[1].append(grid[1][0])
    return newgrid

for c in flip:
    if c == 'H':
        grid = horflip(grid)
        continue
    if c == 'V':
        grid = verflip(grid)
        continue
    
print(f"{str(grid[0][0])} {str(grid[0][1])}")
print(f"{str(grid[1][0])} {str(grid[1][1])}")