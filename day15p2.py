import itertools
def getRobotPos(grid):
    for row in grid:
        if '@' in row:
            return row.index('@'), grid.index(row)
        
def printGrid(grid):
    for row in grid:
        print(''.join(row))

def resize(grid): #returns a new, resized grid according to the specifications
    newgrid = []
    for row in grid:
        newrow = []
        #do stuff
        for tile in row:
            match tile:
                case '#':
                    newrow.append('#')
                    newrow.append('#')
                case 'O':
                    newrow.append('[')
                    newrow.append(']')
                case '.':
                    newrow.append('.')
                    newrow.append('.')
                case '@':
                    newrow.append('@')
                    newrow.append('.')
        newgrid.append(newrow)
    return newgrid
def boxseek(grid, dir, objects):
    x = [0, -1, 0, 1]
    y = [1, 0, -1, 0]
    for obj in objects:
        for j in obj:
            l = None
            r = None
            if grid[j[1] + y[dir]][j[0] + x[dir]] == "[":
                l = (j[0] + x[dir], j[1] + y[dir])
                r = (j[0] + x[dir] +1, j[1] + y[dir]) #right bracket

            elif grid[j[1] + y[dir]][j[0] + x[dir]] == "]":
                r = (j[0] + x[dir], j[1] + y[dir])
                l = (j[0] + x[dir] -1, j[1] + y[dir]) #left bracket
            if l and r and [l,r] not in objects:
                objects.append([l,r])
    return objects
    
def canMove(grid, dir, objects):
    x = [0, -1, 0, 1]
    y = [1, 0, -1, 0]
    merged = list(itertools.chain(*objects)) #turn into a flat list
    for i in merged:
        if grid[i[1] + y[dir]][i[0] + x[dir]] == "#": #if the space any of these is trying to move into is a wall, movement is not possible
            return False
    return True
            


def move(inputs, grid, initX, initY):
    m = len(grid[0])
    n = len(grid)
    xpos = initX
    ypos = initY
    total = len(inputs)
    directions = ["v", "<", "^", ">"] #down left up right
    x = [0, -1, 0, 1]
    y = [1, 0, -1, 0]
    boxes = [']','[']
    for count, move in enumerate(inputs):
        dir = directions.index(move)
        tmpX = xpos + x[dir]
        tmpY = ypos + y[dir]
        objects = [[(xpos,ypos)]] #list of objects to be shifted over - for part 2 instead of tuples it's a list of tuples (to account for boxes)
        objects = boxseek(grid, dir, objects)
        #print(objects)
        if canMove(grid, dir, objects): #only move when there is space available to do so
            #traverse list backwards so everything is always moved into an empty space
            for i in reversed(objects):
                if len(i) > 1:
                    first = i[0] 
                    second = i[1]#because of how we inserted the coordinates, this should always be the rightmost value
                    tmp1 = grid[first[1]][first[0]]
                    tmp2 = grid[second[1]][second[0]]
                    grid[first[1] + y[dir]][first[0] + x[dir]] = tmp1
                    grid[second[1] + y[dir]][second[0] + x[dir]] = tmp2
                    #check to make sure we're not overwriting brackets we want to keep
                    if(second[0] + x[dir], second[1] + y[dir]) != first:
                        grid[first[1]][first[0]] = '.'

                    if(first[0] + x[dir], first[1] + y[dir]) != second:
                        grid[second[1]][second[0]] = '.'
                else:
                    obj = i[0]
                    grid[obj[1] + y[dir]][obj[0] + x[dir]] = grid[obj[1]][obj[0]]
                    grid[obj[1]][obj[0]] = '.' #set to empty space
            xpos += x[dir]
            ypos += y[dir]
        #print(f'Move {move} - {count +1} out of {total}')
        #printGrid(grid)
        #print("\n")
    return grid

def getGPS(grid):
    count = 0
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if grid[i][j] == "[":
                count += (100 * i) + j
    return count




if __name__ == "__main__":
    f = open("inputs/day15input.txt")
    map, inputs = f.read().split("\n\n") #split by double newline
    inputs = list(inputs.replace("\n", "")) #remove all newlines
    grid = [list(line) for line in map.split('\n')]
    grid = resize(grid)
    initX, initY = getRobotPos(grid)
    #print grid initial state
    print("initial state:")
    printGrid(grid)
    grid = move(inputs, grid, initX, initY)
    print("after inputs:")
    printGrid(grid)
    print(getGPS(grid))
