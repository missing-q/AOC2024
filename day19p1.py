import re

if __name__ == "__main__":
    f = open("inputs/day19input.txt")
    towels, tests = f.read().split("\n\n") #split by double newline
    towels = towels.split(", ")
    towels.sort(key=len, reverse=True) #sort by longest string first for our checks
    tests = tests.split("\n")
    r = re.compile("(?:" + "|".join(towels) + ")+") #evil regex magic
    count = 0
    for i in tests:
        if r.fullmatch(i):
            print("Possible!")
            count += 1
        else:
            print("Not possible!")
    print(f'Number of possible designs: {count}')