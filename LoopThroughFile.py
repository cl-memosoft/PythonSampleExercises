file = open('sample.txt')
count = 0

for line in file:
    count = count + 1
print('Line count: ', count)
