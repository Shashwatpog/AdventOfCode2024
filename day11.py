from collections import defaultdict

def isevendigits(n):
    return len(str(n))%2 == 0
def splitn(n):
    n = str(n)
    l = len(n)//2
    return int(n[:l]),int(n[l:])

if __name__ == "__main__":
    #inp = myinput 
    # paste ur input from input file here and separate using ,
    inp = 

    rocks = {rock: 1 for rock in inp}
    for i in range(75):
        newrocks = defaultdict(int)
        for rock,k in rocks.items():
            if rock==0:
                newrocks[1] += k
            elif isevendigits(rock):
                a,b = splitn(rock)
                newrocks[a] += k
                newrocks[b] += k
            else:
                newrocks[rock*2024] = k
        rocks = newrocks
        lr = len(rocks)
        if i == 24:
            print('part1', sum(rocks.values()))
    print('part2', sum(rocks.values()))
