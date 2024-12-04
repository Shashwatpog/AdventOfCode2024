
reports = []
with open('puzz2.txt', 'r') as f:
    for line in f.readlines():
        reports.append([int(z) for z in line.split()])

def safe_check(l):
    n = len(l)
    return ((all(1 <= l[i+1] - l[i] <= 3 for i in range(n-1)))
            or (all(1 <= l[i] - l[i+1] <= 3 for i in range(n-1))))

# part 1
safe1 = sum(map(safe_check, reports))
print(safe1)

# part 2
safe2 = 0
for item in reports:
    safe2 += (safe_check(item)
                    or any(safe_check(item[:i] + item[i+1:]) for i in range(len(item))))
print(safe2)