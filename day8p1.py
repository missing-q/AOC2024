import re
import itertools
import multiprocessing as mp

def getAntinodes(pair, m, n):
    c1 = pair[0]
    c2 = pair[1]

    x1 = c1[0]
    y1 = c1[1]
    x2 = c2[0]
    y2 = c2[1]

    xdiff = x2-x1
    ydiff = y2-y1
    
    temp = [(x1-xdiff, y1-ydiff), (x2+xdiff, y2+ydiff)]
    vals = []
    for i in temp:
        if i[0] < m and i[0] >= 0 and i[1] < n and i[1] >= 0:
            vals.append(i)
    return vals
            
    

    

if __name__ == "__main__":
    antinodes = []
    freqs = {} #list of antennae by frequency. each frequency is a list containing tuples of each antenna coordinate tuned to that frequency.
    grid = [] #keep track
    p = re.compile("[0-9a-zA-Z_]") #alphanumeric
    with open("inputs/day8sample.txt") as f:
        for i, line in enumerate(f):
            grid.append(list(line.strip("\n")))
            for m in p.finditer(line):
                if (str(m.group()) in freqs):
                    freqs[str(m.group())].append((int(m.start()), i))
                else:
                    freqs[str(m.group())] = [(int(m.start()), i)]
    
    #keep track of grid dims for oob
    m = len(grid[0])
    n = len(grid)

    pool = mp.Pool()
    for key, val in freqs.items():
        combinations = list(itertools.combinations(val, r=2))
        result = pool.starmap(getAntinodes, zip(combinations, itertools.repeat(m), itertools.repeat(n)))
        antinodes.append(list(itertools.chain.from_iterable(result)))#un-list everything
        print("antinodes evaluated for frequency " + key)
    antinodes = list(itertools.chain.from_iterable(antinodes)) #double un-list everything
    antinodes = list(dict.fromkeys(antinodes)) #remove duplicates
    print(antinodes)
    print(len(antinodes))
    for i, line in enumerate(grid):
        for j, tile in enumerate(line):
            if (j,i) in antinodes and tile == ".":
                grid[i][j] = "#"
    for line in grid:
        print(''.join(line))
            

