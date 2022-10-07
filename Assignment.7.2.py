# Use the file name mbox-short.txt as the file name
total = 0
cont = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    line = line.rstrip()
    pos = line.find(' ')
    num = line[pos+1:]
    num = float(num)
    total = total + num
    cont =cont + 1
print("Average spam confidence:", float(total)/float(cont))
