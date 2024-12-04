f = open('inputs.txt', 'r')

lines = f.read().splitlines()
lines = [item.strip() for item in lines]

matrix = []
for i in lines:
    matrix.append(list(i))  

#part 1 : logic is to create a matrix and use x and y coordinates to check horizontally, vertically and diagonally for XMAS or SAMX
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'X':
            #horizontal - checks by moving +1 or -1 in x coordinate
            if j + 3 < len(matrix[i]) and matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S':
                count += 1
            if j - 3 >= 0 and matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S':
                count += 1
            #vertical - checks by moving y coordinate by +1 or -1
            if i + 3 < len(matrix) and matrix[i + 1][j] == 'M' and matrix[i + 2][j] == 'A' and matrix[i + 3][j] == 'S':
                count += 1
            if i - 3 >= 0 and matrix[i - 1][j] == 'M' and matrix[i - 2][j] == 'A' and matrix[i - 3][j] == 'S':
                count += 1
            #diagonal from top left to bottom right - checks by moving x coordinate and y coordinate by +1 or -1
            if i + 3 < len(matrix) and j + 3 < len(matrix[i]) and matrix[i + 1][j + 1] == 'M' and matrix[i + 2][j + 2] == 'A' and matrix[i + 3][j + 3] == 'S':
                count += 1
            if i - 3 >= 0 and j - 3 >= 0 and matrix[i - 1][j - 1] == 'M' and matrix[i - 2][j - 2] == 'A' and matrix[i - 3][j - 3] == 'S':
                count += 1
            #diagonal from top right to bottom left - checks by moving x coordinate +1 and y coordinate -1 or x coordinate -1 and y coordinate +1 
            if i + 3 < len(matrix) and j - 3 >= 0 and matrix[i + 1][j - 1] == 'M' and matrix[i + 2][j - 2] == 'A' and matrix[i + 3][j - 3] == 'S':
                count += 1
            if i - 3 >= 0 and j + 3 < len(matrix[i]) and matrix[i - 1][j + 1] == 'M' and matrix[i - 2][j + 2] == 'A' and matrix[i - 3][j + 3] == 'S':
                count += 1
print(count)

#part 2

count2 = 0
flag = False

# M S   M M     S M     S S
#  A     A       A       A       ----> the patterns to find
# M S   S S     S M     M M

patterns = [["M","S","M","S"],
            ["M","M","S","S"],
            ["S","M","S","M"],
            ["S","S","M","M"]
            ]

for y in range(1, len(matrix)-1):
    for x in range(1,len(matrix[y])-1):
        if matrix[y][x] != "A":
            continue
        corner_vals = [matrix[y-1][x-1], matrix[y-1][x+1], matrix[y+1][x-1], matrix[y+1][x+1]] # add all the corner values around "A" into a list 

        if corner_vals in patterns: # check if the corner values match any of the patterns in the patterns list
            count2 += 1
print(count2)            

