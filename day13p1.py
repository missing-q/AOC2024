from sympy import symbols, Eq, solve, Integer
import re

def solveEq(in1, in2):# 2 list of inputs
    x, y = symbols('x,y') 
    # defining equations 
    eq1 = Eq(( (in1[0]*x) + (in1[1]*y) ), in1[2])  
    eq2 = Eq(( (in2[0]*x) + (in2[1]*y) ), in2[2])
    out = solve((eq1, eq2), (x, y))
    
    #if either solution is not an integer then it is not solveable
    if type(out[x]) != Integer or type(out[y]) != Integer:
        return []
    else:
        return [int(out[x]), int(out[y])]


if __name__ == "__main__":
    f = open("inputs/day13input.txt")
    texteqns = f.read().split("\n\n") #split by double newline
    #print(texteqns)
    eqns = []
    for i in texteqns: #convert to ints
        eqns.append([int(s) for s in re.findall(r'\d+', i)])
    #print(eqns)
    a = 3
    b = 1
    #solve each
    count = 0
    for i in eqns:
        x = [i[0], i[2], i[4]]
        y = [i[1], i[3], i[5]]
        out = solveEq(x,y)
        if out != []:
            count += (a * out[0])
            count += (b * out[1])
    print(count)