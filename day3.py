import re
f  = open("inputs.txt","r")

def mul(x,y):
    return x*y
lines = f.read()


# part 1

pattern = "mul\\((\\d+),\\s*(\\d+)\\)"
x =  re.findall(pattern, lines)
s = 0
for i in x:
    s = s + mul(int(i[0]),int(i[1]))
print(s)

#part 2
do = r'do'
dont = r"don't"

total = 0
allowed = True
segments = re.split(f'({dont}|{do})',lines)
pattern = "mul\\((\\d+),\\s*(\\d+)\\)"


for segment in segments:
    
    if "don't" in segment:
        allowed = False
    elif "do" in segment:
        allowed = True
    
    if allowed == True:
        x =  re.findall(pattern, segment)
        for i in x:
            total = total + mul(int(i[0]),int(i[1]))

print(total)