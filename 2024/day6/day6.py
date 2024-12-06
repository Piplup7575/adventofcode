with open("input.txt") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}

# Part 1
start = next(w for w, x in board.items() if x == "^")
walls = {w for w, x in board.items() if x == "#"}
see = set()
z = start
dz = -1
while z in board:
    see.add(z)
    if z + dz in walls:
        dz *= -1j
        continue
    z += dz

print(len(see))


# Part 2
def loops(x):
    new_walls = walls | {x}
    z = start
    dz = -1
    see = set()
    while z in board:
        if (z, dz) in see:
            return True
        see.add((z, dz))
        if z + dz in new_walls:
            dz *= -1j
            continue
        z += dz
    return False

print(sum(map(loops, see)))