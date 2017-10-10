import re

lst = []
total = 0
fh = open("regex_sum_32305.txt", "r")
for line in fh:
    a = re.findall('[0-9]+', line)

    if a != lst:
        lst.extend(a)

list_of_ints = map(int, lst)

for a in list_of_ints:
    total += a

print(total)
