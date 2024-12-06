from collections import defaultdict
from itertools import product

with open("input.txt") as f:
    ls = f.read().strip().split("\n")


b = defaultdict(str)
b |= {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
o = {i + 1j * j for (i, j) in set(product((-1, 0, 1), (-1, 0, 1))) - {(0, 0)}}

# Part 1
print(
    sum(
        [b[z + i * dz] for i in range(4)] == ["X", "M", "A", "S"]
        for z in list(b.keys())
        for dz in object
    )
)


# Part 2
res = 0
for z in list(b.keys()):
    if b[z] == "A":
        corners = [
            b[z + 1 + 1j],
            b[z + 1 - 1j],
            b[z - 1 - 1j],
            b[z - 1 + 1j],
        ]
        if (
            corners.count("M") == 2
            and corners.count("S") == 2
            and b[z - 1 - 1j] != b[z + 1 + 1j]
        ):
            res += 1
print(res)