#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.strip() 

    if not 'From:' in line: #Checks if the first line doesnt have From word
        continue

    words = line.split() #Creates a list of words of a line
    count = count + 1
    print(words[1]) #Prints the character next to from

print('There were', str(count), 'lines in the file with From as the first word')
