fname = input("Enter file name: ")
fh = open(fname)
lst = list()
end = list()
for line in fh:
    lst = line.rstrip().split()
    for  l in lst:
        if l not in end:
            end.append(l)
end.sort()
print(end)
