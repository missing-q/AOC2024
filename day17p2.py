import re
from sys import maxsize
class computer:
    def __init__(self, regA, regB, regC):
        self.reg_A = regA
        self.reg_B = regB
        self.reg_C = regC
        self.ip = 0
        self.output = [] #turn this into a string later
    
    def getCombo(self, op):
        match op:
            case 0: return 0
            case 1: return 1
            case 2: return 2
            case 3: return 3
            case 4: return self.reg_A
            case 5: return self.reg_B
            case 6: return self.reg_C
            case 7: return -1

    def parseInst(self, inst, op):
        match inst:
            case 0:  #A division
                num = self.reg_A
                denom = pow(2, self.getCombo(op))
                self.reg_A = int(num/denom)
                self.ip += 2 #increment instruction pointer
            case 1: #bitwise xor
                self.reg_B ^= op
                self.ip += 2 #increment instruction pointer
            case 2: #bst
                self.reg_B = self.getCombo(op) % 8
                self.ip += 2 #increment instruction pointer
            case 3: #jump if not zero
                if self.reg_A != 0:
                    self.ip = op
                else: #no jump, increase IP
                    self.ip += 2 #increment instruction pointer
            case 4: #bitwise xor of B and C, don't do anything with the operand
                self.reg_B ^= self.reg_C
                self.ip += 2 #increment instruction pointer
            case 5: #output
                self.output.append(self.getCombo(op) % 8)
                self.ip += 2 #increment instruction pointer
            case 6: #B division, stores in the B register instead of A (numerator still is A)
                num = self.reg_A
                denom = pow(2, self.getCombo(op))
                self.reg_B = int(num/denom)
                self.ip += 2 #increment instruction pointer
            case 7: #C division, stores in the C register instead of A (numerator still is A)
                num = self.reg_A
                denom = pow(2, self.getCombo(op))
                self.reg_C = int(num/denom)
                self.ip += 2 #increment instruction pointer
        
    def parseProgram(self, program):
        length = len(program) - 1 #past this point the program should halt
        while self.ip < length:
            inst = program[self.ip]
            op = program[self.ip + 1]
            self.parseInst(inst, op)

        #print(','.join(map(str, self.output))) #parse output
        return self.output

            
def reverseEngineer(program): #will return the value of A required to match input
    valid_As = {0}
    for inst in reversed(program): #walk backwards through program instructions
        nextVals = set()
        for a_val in valid_As:
            aShift = a_val * 8 #since the last instruction modifying A is //8, we "reverse" that here
            for candidate in range(aShift, aShift+8): #try all possible values of a that can yield a//8 = 0
                testout = computer(candidate, 0, 0).parseProgram(program)
                if testout and testout[0] == inst: #compare against "canon" instructions
                    nextVals.add(candidate) #if yes, then add it as a possible candidate to test next
        valid_As = nextVals
    #print(valid_As) #all values of a that will yield the input as output
    return min(valid_As)


if __name__ == "__main__":
    f = open("inputs/day17input.txt")
    init, program = f.read().split("\n\n") #split by double newline
    regA, regB, regC = [int(s) for s in re.findall(r'\d+', init)]
    program = [int(s) for s in re.findall(r'\d+', program)]
    comp = computer(regA, regB, regC)
    out = comp.parseProgram(program)
    print(len(program))
    print(reverseEngineer(program))
    
    
