# import
# honestly the coolest thing about aoc is how many new python modules i'm finding that do exactly what i need them to do
import itertools
import math
import re

# read inputs (replace my input with your input from the website in this file)
with open("input.txt") as inputs:
    ls = inputs.read().strip().split("\n")

# grid - exclude . symbol
grid = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
partssymbol = {
    (i, j): (x, [])
    for i, l in enumerate(ls)
    for j, x in enumerate(l)
    if x != "." and not x.isdigit()
}

# vars
partsum = 0
for i, l in enumerate(ls):
    for match in re.finditer(r"\d+", l):
        n = int(match.group(0))
        boundary = {
            (i + di, j + dj)
            for di, dj in grid
            for j in range(match.start(), match.end())
        }
        if partssymbol.keys() & boundary:
            partsum += n
        for symbol in partssymbol.keys() & boundary:
            partssymbol[symbol][1].append(n)

# print solutions - my input should give 538046
print(partsum)

# part 2, print - my input should give 81709807
# only looking for * symbol touching two numbers
print(
    sum(
        math.prod(parts)
        for symbol, parts in partssymbol.values()
        if len(parts) == 2 and symbol == "*"
    )
)