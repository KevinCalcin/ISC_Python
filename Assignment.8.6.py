fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
mails = dict()
max = None
word = None

for line in fh:
    line = line.rstrip()
    lst = line.split()
    if line.startswith('From') and len(lst) > 2:
        for mail in lst[1:2]:
            mails[mail] = mails.get(mail,0) + 1


for mail,t in mails.items():
    if word is None or t > max:
        max = t
        word = mail

print(word,max)
