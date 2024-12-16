import re
import math
from collections import Counter
def printGridState(m, n, robots):
    printgrid = []
    for i in range(n):
        line = []
        for j in range(m):
            count = 0
            for robot in robots:
                if robot[0] == (j,i):
                    count += 1
            if count == 0:
                line.append('.')
            else:
                line.append(str(count))
        printgrid.append(line)
    for i in printgrid:
        print(''.join(i))

def iterate(robots, m, n): #list of all robots, number of loops, grid dims
    count = 0 #count seconds
    while any(count > 1 for count in Counter([x[0] for x in robots]).values()): #keep going until there are no more overlapping robots
        count += 1
        #loop thru all robots
        for idx, robot in enumerate(robots):
            newX = robot[0][0] + robot[1][0] #current x plus x velocity
            newY = robot[0][1] + robot[1][1] #current y plus y velocity
            #wrap around xwise
            if newX >= m: 
                newX -= m
            elif newX < 0:
                newX += m
            
            #wrap around ywise
            if newY >= n: 
                newY -= n
            elif newY < 0:
                newY += n

            robots[idx][0] = (newX, newY)
    return robots, count

def getSafetyFactor(robots, m, n):
    middleX = m//2
    middleY = n//2
    quadrants = [0,0,0,0]
    for robot in robots:
        xpos = robot[0][0]
        ypos = robot[0][1]
        quad = 0
        if xpos != middleX and ypos != middleY: #dont count robots in the middle axes
            if xpos > middleX:
                if ypos > middleY:
                    quad = 3
                else:
                    quad = 1
            else:
                if ypos > middleY:
                    quad = 2
                else:
                    quad = 0
            quadrants[quad] += 1
    return math.prod(quadrants)

            


if __name__ == "__main__":
    f = open("inputs/day14input.txt")
    textin = f.read().split("\n") #split by double newline
    #print(texteqns)
    m = 101 #101 in real input
    n = 103 #103 in real input
    #initialize grid
    #print(grid)
    robots = []
    for i in textin: #formatting
        tmp = [int(s) for s in re.findall(r'-?\d+', i)]
        #print(tmp)
        robots.append([(tmp[0],tmp[1]),(tmp[2],tmp[3])]) #pos, vel
    print("before iterations:")
    #print(robots)
    printGridState(m,n,robots)
    robots, count = iterate(robots, m, n)
    print("after iterations:")
    #print(robots)
    
    printGridState(m,n,robots)
    print(getSafetyFactor(robots, m, n))
    print(count)

