# Python Dictionaries
# dict() - calling dictionary function

#ex 1 - Checks the value. If the value doesn't exist, a new name will be added to the dictionary.
#If the value already exists, the count will be incremented
jojoCount = dict()
names = {'Jonathan', 'Joseph', 'Jotaro', 'Josuke', 'Jolynne'}

for name in names:
    if not name in jojoCount:
        jojoCount[name] = 1
    else:
        jojoCount[name] = jojoCount[name] + 1

print('>' + str(jojoCount))

print('#####################') #### space

## Below is to check whether the key exists or not. If the value already exists, it c
#using the long method
counts = dict()
counts = {'DIO': 5}
namae = {'Speedwagon': 1, 'DIO': 1, 'Kakyoin': 1, 'Iggy': 1}

print(namae.keys())

print('#####################')

for n in namae:
    if n in counts:
        x = counts[n] #sets the value to the value of counts if the key is in the counts
        namae[n] = namae[n] + counts[n]
    else:
        x = 0 #sets the default value to default if doesn't exists
    print('>' + str(x))
    continue
print(namae)

print('#####################') #### space

#using get() method
for n in namae:
    y = counts.get(n, 0) #if the 'n' exists in counts, it will get its value and assign it to x. If not, it will create another x but the default values are 0
    print('>' + str(y))
    continue

print('#####################')
# Using len() method to determine how many items a dictionary has
print(len(namae))


print('#####################')
# Adding item to a dictionary
count = 4

for x in range(count):
    namae['Polnareff'] = x + 1

print(namae)

print('#####################')
# Using the update() method to add item to dictionary
namae.update({'Avdol' : 23})
print(namae)
#Exercise: Enter many names in a Dictionary. If the name already exists, update the count, if not, create another one. If the user presses 'done', print the dictionary and count per line.
