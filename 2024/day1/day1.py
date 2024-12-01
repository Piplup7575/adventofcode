from collections import Counter

left = []
right = []

# open and add values to lists
with open('input.txt') as f:
    for i in f:
        num = list(map(int, i.split()))
        left.append(num[0])
        right.append(num[1])

# solve part 1 - sort values, compare, sum
def p1(l, r):
    l.sort()
    r.sort()
    p1 = sum(abs(l - r) for l, r in zip(l, r))
    return p1

# solve part 2 - calculate similarity score
def p2(l, r):
    rCount = Counter(r)
    p2 = sum(i * rCount[i] for i in l)
    return p2

# print solves
p1 = p1(left, right)
print(f"{p1}")
p2 = p2(left, right)
print(f"{p2}")