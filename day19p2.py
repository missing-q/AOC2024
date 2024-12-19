import re
import multiprocessing as mp
from itertools import repeat
#trie data structure & ways of forming string code borrowed from https://www.geeksforgeeks.org/number-of-ways-to-form-a-given-string-from-the-given-set-of-strings/ :)

# Trie data structure
class Trie:
    def __init__(self):
        self.end = False
        self.children = [None]*26
 
# Inserting the strings into trie
def insert(root, s):
    n = len(s)
    prev = root
    for i in range(n):
        index = ord(s[i]) - ord('a')
        if prev.children[index] is None:
            prev.children[index] = Trie()
        prev = prev.children[index]
    prev.end = True
 
# Function to find number of ways of forming string str
def waysOfFormingString(root, s):
    n = len(s)
 
    # Count[] to store the answer
    # of prefix string str[0....i]
    count = [0]*n
    for i in range(n):
        ptr = root
        for j in range(i, -1, -1):
            ch = s[j]
 
            # If not found, break
            # out from loop
            index = ord(ch) - ord('a')
            if ptr.children[index] is None:
                break
            ptr = ptr.children[index]
 
            # String found, update the
            # count(i)
            if ptr.end:
                if j > 0:
                    count[i] += count[j - 1]
                else:
                    count[i] += 1
    return count[n - 1]
 


         
if __name__ == "__main__":
    f = open("inputs/day19input.txt")
    towels, tests = f.read().split("\n\n") #split by double newline
    towels = towels.split(", ")
    towels.sort(key=len, reverse=True) #sort by longest string first for our checks
    longest_str = len(towels[0])
    
    tests = tests.split("\n")
    r = re.compile("(?:" + "|".join(towels) + ")+") #evil regex magic
    count = 0
    part2_tests = []
    for i in tests:
        if r.fullmatch(i):
            print("Possible!")
            part2_tests.append(i)
            count += 1
        else:
            print("Not possible!")
    
    #doing part 2 things...
    #construct trie
    root = Trie()
    for i in range(len(towels)):
        insert(root, towels[i][::-1])
    
    permutations = 0
    for i in part2_tests:
        permutations += waysOfFormingString(root, i)
    print(f'Number of possible designs: {count}')
    print(f'Number of design permutations: {permutations}')