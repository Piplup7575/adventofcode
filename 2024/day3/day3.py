import re

with open("input.txt") as f:
    data = f.read()

def solve(b):
    out = 0
    do = True
    # i love regex i love regex i love regex i love regex (please save me)
    # find all mul() functions that are properly formatted ( mul(\d+, \d+) )
    # find all do() and all don't()
    for i, j, k in re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data):
        # check if valid
        if i == "don't()":
            do = False
        elif i == "do()":
            do = True
        else:
            # if allowed, multiply and add mul() together
            if do or b:
                out += int(j) * int(k)
    return out

# print solves
print(f"{solve(True)}")
print(f"{solve(False)}")