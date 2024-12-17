import heapq
directions = ["v", "<", "^", ">"] #down left up right
xdirs = [0, -1, 0, 1]
ydirs = [1, 0, -1, 0]

class Node:
    def __init__(self, x, y, direction=None):
        self.x = x
        self.y = y
        self.g = 0  # Cost from start
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost (g + h)
        self.parent = None
        self.direction = direction  # Track direction to calculate turn cost

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, goal, turn_cost):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add((current_node.x, current_node.y))

        if current_node == goal:
            return reconstPath(current_node)

        for neighbor in getNeighbors(grid, current_node):
            if (neighbor.x, neighbor.y) in closed_set:
                continue

            new_g = current_node.g + 1
            if neighbor.direction != current_node.direction:
                new_g += turn_cost  # Add turn cost if direction changes

            if neighbor not in open_list or new_g < neighbor.g:
                neighbor.g = new_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node
                neighbor.direction = getDirection(current_node, neighbor)
                if neighbor not in open_list:
                    heapq.heappush(open_list, neighbor)

    return None  # No path found

def reconstPath(node):
    path = []
    while node is not None:
        path.append(node)
        node = node.parent
    return path[::-1]

def getNeighbors(grid, node):
    # Implement logic to get valid neighbors based on grid and movement rules
    originX = node.x
    originY = node.x
    m = len(grid[0])
    n= len(grid)
    adj = set()
    for i in range(4):
        if originX + xdirs[i] < m and originX + xdirs[i] >= 0 and originY + ydirs[i] < n and originY + ydirs[i] >= 0:
            if grid[originX + xdirs[i]][originY + ydirs[i]] != "#":
                tmp = Node(originX + xdirs[i], originY + originX[i], i)
                adj.add(tmp)
    return adj

def heuristic(node, goal):
    #manh dist
    return abs(goal.x - node.x) + abs(goal.y - node.y)

def getDirection(node1, node2):
    # calc direction
    xdiff = node2.x - node1.x
    ydiff = node2.y - node1.y
    for i in range(4):
        if xdiff==xdirs[i] and ydiff == ydirs[i]:
            return i
def getPos(char, grid):
    for row in grid:
        if char in row:
            return row.index(char), grid.index(row)

if __name__ == "__main__":
    grid = [] #keep track
    with open("inputs/day16sample.txt") as f:
        for i, line in enumerate(f):
            grid.append(list(line.strip("\n")))
    start = getPos('S', grid)
    end = getPos('E', grid)
    startNode = Node(start[0], start[1], 3)
    endNode = Node(end[0], end[1])
    path = astar(grid, startNode, endNode, 1000)