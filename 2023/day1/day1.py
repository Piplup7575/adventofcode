# import regrex
import re

# read inputs (replace my input with your input from the website in this file)
with open("input.txt") as f:
    data = f.read().strip()

# split out numbers from words, then add them
def solve(data):
    ls = data.split("\n")
    ns = [re.findall("\d", x) for x in ls]
    return sum(int(n[0] + n[-1]) for n in ns)

# print in console solutions - my input should give 54630
print("part 1")
print(solve(data))
# took me about 2 hours for this lol

# part two asks for numbers in text form as apposed to the numbers
# just replace the numbers found with the input.txt file with a readable number
# replace "one" with "one1one" so if there is an edge case where it needs the
# last part of the word to make another number it can still read it
data = (
    data.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)

# print - my input should give 54770
print("part 2")
print(solve(data))
