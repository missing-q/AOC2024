from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder



if __name__ == "__main__":
    size = 71
    limit = 1024
    inputgrid = [ [1]*size for i in range(size)]
    with open("inputs/day18input.txt") as f:
        for i, line in enumerate(f):
            if i < limit:
                wall = tuple(int(s) for s in line.strip("\n").split(','))
                inputgrid[wall[1]][wall[0]] = 0
    grid = Grid(matrix=inputgrid)
    start = grid.node(0,0)
    end = grid.node(size-1,size-1)
    finder = AStarFinder()
    path, runs = finder.find_path(start,end,grid)
    print('operations:', runs, 'path length:', len(path)-1)
    print(grid.grid_str(path=path, start=start, end=end))
    