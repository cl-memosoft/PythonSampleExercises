# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
txt = input('Please input file name: ')
fil = open(txt)

wlist = list()

for line in fil:
    r = line.strip().split()

    for x in r:
        if x in wlist:
            continue
        else:
            wlist.append(x)


wlist.sort()
print(wlist)
