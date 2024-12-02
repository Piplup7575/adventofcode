safe1 = 0
safe2 = 0

# part1
def p1(r):
    # check if all numbers increment or decrement
    inc = all(r[i] < r[i+1] for i in range(len(r) - 1))
    dec = all(r[i] > r[i+1] for i in range(len(r) - 1))
    if (inc or dec) != True:  
        return False

    # check if numbers only differ by 1-3 between each
    for i in range(len(r) - 1):
        dif = abs(r[i] - r[i+1])
        if dif < 1 or dif > 3:
            return False
    
    return True
    
# part2
def p2(r):
    for i in range(len(r)):
        # check if a unsafe row returns true if one number is ignored 
        q = r[:i] + r[i+1:]
        if p1(q):
            return True
    return False

# open and calculate
with open('input.txt') as f:
    for i in f:
        r = list(map(int, i.split()))

        if p1(r):
            safe1 += 1
        elif p2(r):
            safe2 += 1

# part 1
print(f"{safe1}")
print(f"{safe1 + safe2}")