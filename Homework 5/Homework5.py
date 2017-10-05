import re

lst = []
fh = open("file.txt", "r")
for line in fh:
    a = re.findall('[0-9]+', 'line')
    if a != []:
        lst.extend(a)
    total = 0
    for a in lst:
        total = total + a
