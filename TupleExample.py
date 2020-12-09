# Assigning a simple tuple
food = ('apple', 'banana', 'mango')

for x in food:
    print(x) #to print the iteration, you dont need to do : food[x]


# Assigning multiple values
(x, y, z) = ('apple', 'banana', 'mango')
print(x, y, x)


# Comparing Tuples
x = (5, 4, 4)
y = (5, 2, 5)

if x < y:
    print('y is greater than x')

else:
    print('x is greater than y')


# Sorting Lists of Tuples by using For loop
dic = {'a' : 9, 'b' : 8, 'c' : 7}
final = sorted(dic.items()) #Gets the list of items of a dictionary

print(final)

# Another way to sort lists of Tuples
for a, b in sorted(dic.items()):
    print(a, b)

#Sorting by Values Instead of Keys
samplelist = list()

for k, v in dic.items():
    samplelist.append((v, k)) #Add values to a list by putting values first then key.
                              #Use '()' because append() only takes 1 argument and and also,
                              #You're passing both the key and value as one
print(samplelist)

samplelist = sorted(samplelist) #Since list is mutable and can be ordered, we are allowed to Use
                                                #The sorted() function.
print(samplelist)
