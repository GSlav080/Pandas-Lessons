import sys

count = 0
i = -1
l = 0
mass = []
for line in sys.stdin:
    i+=1
    string = [i for i in list(map(int, line.split(' '))) if i % 7 == 0]
    a, b = string, len(string)
    mass += [a]
    if(l<b):
        l = b
        count = i

otv = mass[count]
otv = str(otv).replace("[", '').replace("]", '')
print(otv)


