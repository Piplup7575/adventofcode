# import
import math
import re
from collections import defaultdict

# read inputs (replace my input with your input from the website in this file)
with open("input.txt") as inputs:
    ls = inputs.read().strip().split("\n")

# vars
ids = 0
powersum = 0
for l in ls:
    # regex1!1!1!1!111!1
    parts = re.sub("[;,:]", "", l).split()
    maxcolor = defaultdict(int)
    for count, color in zip(parts[2::2], parts[3::2]):
        maxcolor[color] = max(maxcolor[color], int(count))
    # compare
    if maxcolor["red"] <= 12 and maxcolor["green"] <= 13 and maxcolor["blue"] <= 14:
        ids += int(parts[1])
    # part 2
    powersum += math.prod(maxcolor.values())

# print in console solutions - my input should give 2683
print("part 1")
print(ids)

# print - my input should give 49710
print("part 2")
print(powersum)