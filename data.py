import re

fname = input("Enter file name: ")
fh = open(fname)

result = list()
total = 0
count = 0
for line in fh:
    result = re.findall('[0-9]+',line)
    count = count + len(result)
    for num in result:
        total = total + int(num)

print('numero enteros:',count,'suma total:',total)
