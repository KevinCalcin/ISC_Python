fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
hours = dict()
for line in fh:
    line = line.rstrip()
    lst = line.split()
    if line.startswith('From') and len(lst) > 2:
        lst = lst[5:6]
        for line in lst:
            h = line.split(':')
            for hour in h[0:1]:
                hours[hour] = hours.get(hour,0) + 1

lst = list()

for key,value in hours.items():
    h = (key,value)
    lst.append(h)

lst = sorted(lst,reverse =False)

for x,y in lst:
    print(x,y)
