import re
m=input("GIve your File name")
handle = open(m)
sum = 0
count = 0
m = handle.read()
words = m.split()
for word in words:
    y = re.findall('[0-9]+', word)

    for x in y:
        sum = sum + int(x)
        count = count + 1

print(sum)
print('Average', sum / count)

