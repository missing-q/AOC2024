import multiprocessing as mp
import itertools

def operatorIters(num):
    yield from itertools.product(*(["+*|"] * num))

def evalLTR(soln, equation):
    operator = "+" #start off as a sum so we add the first number 
    sum = 0
    temp = list(equation)
    for i in temp:
        if i == "+" or i == "*" or i == "|":
            operator = i
        else:
            num = int(i)
            match operator:
                case "+":
                    sum += num
                case "*":
                    sum *= num
                case "|":
                    sum = int(str(sum) + str(num)) #concatenation
    return soln == sum


def iterateEqns(soln, equation):
    num = equation.count(" ") #number of empty spaces to insert
    combinations = list(operatorIters(num))
    pool = mp.Pool()
    testeqs = []
    for i, variant in enumerate(combinations):
        testeq = equation.split(" ")
        index = 1 #keep track of next place to insert the operator
        for operator in variant:
            testeq.insert(index,operator)
            index += 2
        testeqs.append(testeq)
    for result in pool.starmap(evalLTR, zip(itertools.repeat(soln), testeqs)):
        if result:
            pool.close()
            pool.join()
            print("solution found for " + str(soln))
            return True
    print("no solution for " + str(soln))
    return False
        


if __name__ == "__main__":
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
            print("........equation " + str(i+1) +  " out of " + str(len(eqns)))

    print(sum)