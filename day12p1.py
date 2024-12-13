import re

def getPerimeter(region, m, n): #input - list of tuples coordinates, int int grid dims
    perimeter = 0
    for tile in region:
        adj = adjacent(tile, m, n)
        for i in adj:
            if not i in region: #dont draw perimeter between two squares of the same region
                perimeter += 1
        perimeter += 4-len(adj) #also draw perimeter for any tiles against the grid edges
    return perimeter

def adjacent(square, m, n): #input: tuple, int int - origin square, grid dimensions - output: list of tuples containing the coords of adjacent squares
    #left down up right
    x = [-1,0,0,1]
    y = [0,1,-1,0]
    originX = square[0]
    originY = square[1]
    adj = []
    for i in range(4):
        if originX + x[i] < m and originX + x[i] >= 0 and originY + y[i] < n and originY + y[i] >= 0:
            adj.append((originX + x[i], originY + y[i]))
    return adj

def getRegion(tile, grid, region): #input: origin tile, grid, list - output: list
    adj = adjacent(tile, len(grid[0]), len(grid))
    char = grid[tile[1]][tile[0]]
    for i in adj:
        if grid[i[1]][i[0]] == char:
            if i not in region:
                region.append(i)
                region + getRegion(i, grid, region)
    return region

def countRegionType(char, d):
    count = 0
    for key in d.keys():
        count += key.count(char)
    return count

def getRegionsDict(regions, grid): #input: dict, grid
    for i, line in enumerate(grid):
        for j, tile in enumerate(line):
            if not any((j,i) in value for value in regions.values()): #if tile is not in any region's list
                region = getRegion((j,i), grid, [(j,i)])
                if tile in regions: #do we have a region of the same name?
                    name = tile + str(countRegionType(tile, regions) + 1) #R2, R3, etc...
                    regions[name] = region
                else:
                    regions[tile] = region
    return regions


    
if __name__ == "__main__":
    antinodes = []
    regions = {} #dict of regions. each region contains all a list of all tiles in that region
    grid = [] #keep track
    p = re.compile("[0-9a-zA-Z_]") #alphanumeric
    with open("inputs/day12input.txt") as f:
        for i, line in enumerate(f):
            grid.append(list(line.strip("\n")))
    
    m, n = len(grid[0]), len(grid)
    regions = getRegionsDict(regions, grid)
    print (regions)
    count = 0
    for key, val in regions.items():
        area = len(val)
        perimeter = getPerimeter(val, m, n)
        print(f'{key} - {area} - {perimeter}')
        count += area*perimeter
    print(f'total is {count}')