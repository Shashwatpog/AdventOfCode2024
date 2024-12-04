f = open("puzz1.txt","r")
l = []
l1 = []
l2 = []

for i in range(0,1000):
    l = l + f.readline().split("   ")
l = [int(i.strip()) for i in l]


for i in range(0,len(l)):
    if i % 2 == 0:
        l1.append(l[i])
    else:
        l2.append(l[i])

l1.sort()
l2.sort()

# puzzle 1

sum_of_diff = 0

for i in range(len(l1)):
    sum_of_diff += abs(l1[i] - l2[i])

print(sum_of_diff)


# puzzle 2

sum_of_similarity = 0

for i in range(len(l1)):
    sum_of_similarity += (l1[i] * l2.count(l1[i]))
print(sum_of_similarity)