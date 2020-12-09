# Combining the use of Dictionaries and Files
# Notice: This code doesn't work on Python 2.7 and below

jojoCounts = dict()
chars = input('Enter JoJo characters: ')
jchars = chars.split() #This is to convert input characters to list

print(jchars)

for word in jchars:
    jojoCounts[word] = jojoCounts.get(word, 0) + 1 # Creates dictionary out of the values og the list
print('Counts', jojoCounts)

# jonathan joseph joseph joseph jotaro jonathan jonathan josuke jotaro
# jonathan jotaro jonathan joseuke joseph jonathan

# simulated: jonathan: 1, joseph 2, ===> The simulation goes on

#### Exercise: Follow the instructions
## Check box below if it succeeds
# [x] Read a File
# [x] Read every words in the File
# [x] Create a list of words using the values of the File
# [x] Create a dictionary using the list created to get the count of every word
# [x] Get and print the word with the highest count

print('Please input file: ')
infile = open(input())
indict = dict()

for word in infile:
    w = word.split()

    for x in w:
        indict[x] = indict.get(x, 0) + 1

highestval = None
higestword = None

for word,val in indict.items(): # Use items function to loop through the dictionary items
    if highestval is None or val > highestval:
        highestword = word
        highestval = val
print('The word with the highest count is "', highestword, '" : ', highestval)
