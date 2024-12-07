import re
import itertools

def operatorIters(num):
    yield from itertools.product(*(["+*"] * num))

def evalLTR(soln, equation):
    operator = "+" #start off as a sum so we add the first number 
    sum = 0
    temp = list(equation)
    for i in temp:
        if i == "+" or i == "*":
            operator = i
        else:
            num = int(i)
            if operator == "+":
                sum += num
            else:
                sum *= num
    return soln == sum


def iterateEqns(soln, equation):
    num = equation.count(" ") #number of empty spaces to insert
    combinations = list(operatorIters(num))
    for i, variant in enumerate(combinations):
        testeq = equation.split(" ")
        index = 1 #keep track of next place to insert the operator
        for operator in variant:
            testeq.insert(index,operator)
            index += 2
        if evalLTR(soln, testeq):
            return True
        
    return False
        



solns = []
eqns = []
sum = 0
#feed into arrays
with open("inputs/day7input.txt") as f:
    for line in f:
        solution, equation = line.split(": ")
        solns.append(int(solution))
        eqns.append(equation.strip("\n"))


for i, eqn in enumerate(eqns):
    if iterateEqns(solns[i], eqn):
        sum += solns[i]

print(sum)