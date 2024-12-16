def getRobotPos(grid):
    for row in grid:
        if '@' in row:
            return row.index('@'), grid.index(row)
        
def printGrid(grid):
    for row in grid:
        print(''.join(row))
        
        
def move(inputs, grid, initX, initY):
    m = len(grid[0])
    n = len(grid)
    xpos = initX
    ypos = initY
    directions = ["v", "<", "^", ">"] #down left up right
    x = [0, -1, 0, 1]
    y = [1, 0, -1, 0]
    for move in inputs:
        dir = directions.index(move)
        tmpX = xpos + x[dir]
        tmpY = ypos + y[dir]
        objects = [(xpos,ypos)] #list of objects to be shifted over
        while grid[tmpY][tmpX] == 'O':
            objects.append((tmpX, tmpY))
            tmpX += x[dir]
            tmpY += y[dir]
        if grid[objects[-1][1] + y[dir]][objects[-1][0] + x[dir]] == '.': #only move when there is space available to do so
            #traverse list backwards so everything is always moved into an empty space
            for i in reversed(objects):
                grid[i[1] + y[dir]][i[0] + x[dir]] = grid[i[1]][i[0]]
                grid[i[1]][i[0]] = '.' #set to empty space
            xpos += x[dir]
            ypos += y[dir]
        #print(f'Move {move}:')
        #printGrid(grid)
        #print("\n")
    return grid

def getGPS(grid):
    count = 0
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if grid[i][j] == "O":
                count += (100 * i) + j
    return count




if __name__ == "__main__":
    f = open("inputs/day15input.txt")
    map, inputs = f.read().split("\n\n") #split by double newline
    inputs = list(inputs.replace("\n", "")) #remove all newlines
    grid = [list(line) for line in map.split('\n')]
    initX, initY = getRobotPos(grid)
    #print grid initial state
    print("initial state:")
    printGrid(grid)
    grid = move(inputs, grid, initX, initY)
    print("after inputs:")
    printGrid(grid)
    print(getGPS(grid))
