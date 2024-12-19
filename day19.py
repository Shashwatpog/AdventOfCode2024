from functools import cache

patterns = []

with open("input.txt","r") as f:
    towels = f.readline().strip().split(", ")
    f.readline()
    for line in f.readlines():
        patterns.append(line.strip())

# using memoization with functools cache
@cache
def no_of_arrangements(pattern,start=0):
    if start >= len(pattern):
        return 1
    result = 0
    for i in towels:
        if pattern[start:start+len(i)] == i:
            result += no_of_arrangements(pattern,start+len(i)) # recursion with memoization
    return result

# Part 1 answer
print(sum(no_of_arrangements(pattern)>0 for pattern in patterns))

# simple part 2 by mapping
print(sum(map(no_of_arrangements,patterns)))

