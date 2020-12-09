import re

#using search
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)


#using findall function
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()

    x = re.findall("^From", line)
print(x)


#using split
txt = "The rain in Spain"
x = re.split("\s", txt, 1) #splits at each whitespace character
print(x)


#using sub()
y = re.sub("in", "cute", txt, 3)
print(y)

#using match
