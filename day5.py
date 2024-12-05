f = open("inputs.txt","r")

lines = f.readlines()
rules = []

# get index of where the line break between rules and page updates is 
for i in range(len(lines)):
    if lines[i]== "\n":
        index_of_newline = i

# add all rules into a list 
for i in range(index_of_newline):
    line = lines[i].split("|")
    temp = [int(item.strip()) for item in line]
    rules.append(temp)

# PART 1

# initialize an empty list to store all valid page updates 
pages = []

# iterate through the page updates and check the rules for validity 
for i in range(index_of_newline + 1, len(lines)):
    #parse and clean
    line = lines[i].split(",")
    line = [int(item.strip()) for item in line]
    #check if the nth and n+1th element are in the rules list and not the other way arround based on the rules provided
    for i in range(len(line)-1):  
        if [line[i],line[i+1]] in rules and [line[i+1],line[i]] not in rules :  
            # if satisfies this add it to a list, if already in the list leave it there
            if line in pages:
                continue
            else:
                pages.append(line)                
        else:                   
            # if not remove it from the list if it was added earlier or else break    
            if line in pages:
                pages.remove(line)
            break

count = 0
#print(pages) # logging the pages that are valid 

# find the mid index of each valid page update and sum it up
for i in pages:
    mid_index = (len(i)-1)/2
    count+= i[int(mid_index)]
print(count)

# PART 2 

# swap 2 numbers functions
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

# function to swap nth and n-1th element to correct the order
def correct(x,rules,result):
    for i in range(1,len(x)):
        if [x[i],x[i-1]] in rules:
            x[i],x[i-1] = swap(x[i],x[i-1])
            # use recursion to keep swapping until correct order is achieved 
            correct(x,rules,result)
        else:
            continue
        if x not in result:
            result.append(x)
    return result

# corrected order list initialized
corrected = []

for i in range(index_of_newline + 1, len(lines)):
    #parse and clean
    line = lines[i].split(",")
    line = [int(item.strip()) for item in line]
    # call correct() function and pass the arguments and a list of corrected orders is returned
    correct(line,rules,corrected)

corrected_count = 0
# sum the element in the middle of the each order
for i in corrected:
    mid_index = (len(i)-1)/2
    corrected_count += i[int(mid_index)]
print(corrected_count)


f.close()