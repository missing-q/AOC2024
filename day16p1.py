from enum import Enum
import heapq
from sys import maxsize
from collections import defaultdict

def getPos(char, grid):
    for row in grid:
        if char in row:
            return row.index(char), grid.index(row)
def getWalls(char, grid):
    walls = set()
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if tile == char:
                walls.add((j,i))
    return walls

if __name__ == "__main__":
    grid = [] #keep track
    with open("inputs/day16sample.txt") as f:
        for i, line in enumerate(f):
            grid.append(list(line.strip("\n")))
    start = getPos('S', grid)
    end = getPos('E', grid)
    walls = getWalls('#', grid)
    #print(walls)

#define coordinate type
coord = tuple[int,int]

class dirs(Enum):
    down = (0, 1)
    left = (-1, 0)
    up = (0, -1)
    right = (1, 0)

    def turnCW(self):
        dir = self
        match dir:
            case dirs.down: dir = dirs.left
            case dirs.left: dir = dirs.up
            case dirs.up: dir = dirs.right
            case dirs.right: dir = dirs.down
        return dir
    
    def turnCCW(self):
        dir = self
        match dir:
            case dirs.down: dir = dirs.right
            case dirs.right: dir = dirs.up
            case dirs.up: dir = dirs.left
            case dirs.left: dir = dirs.down
        return dir

    def distTo(self, coord): #of type coord aka tuple of ints
        x, y = coord
        x2, y2 = self.value
        return (x + x2, y + y2)
    
    def backTrack(self, coord): #for tracing all the paths back
        x, y = coord
        x2, y2 = self.value
        return (x - x2, y - y2)

    
direction = dirs.right
#define coordinate-direction pair
pair = tuple[coord,direction]

distances: dict[pair, int] = defaultdict(lambda: 999999999999999)
distances[(start, direction)] = 0 #distance from the starting point will always be 0
open_list = {(start, direction),}

while open_list:
    newcoord, direction = open_list.pop()
    num = distances[newcoord, direction]

    # check forward
    forward = direction.distTo(newcoord)
    if forward not in walls:
        new_distance = num + 1
        if distances[forward, direction] > new_distance:
            distances[forward, direction] = new_distance
            open_list.add((forward, direction))

    # check clockwise turn
    cw = direction.turnCW() 
    if cw.distTo(newcoord) not in walls:
        new_distance = num + 1000 #turn incurs 1000 penalty
        if distances[newcoord, cw] > new_distance:
            distances[newcoord, cw] = new_distance
            open_list.add((newcoord, cw))

    # check ccw turn
    ccw = direction.turnCCW() 
    if ccw.distTo(newcoord) not in walls:
        new_distance = num + 1000 #turn incurs 1000 penalty
        if distances[newcoord, ccw] > new_distance:
            distances[newcoord, ccw] = new_distance
            open_list.add((newcoord, ccw))
    #print(open_list)
print(distances[end,dirs.up])

        
