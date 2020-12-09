# using split to split string variable into an array
jojos = 'Jonathan joestar best jojo'
jojoCap = jojos.upper()
jojo = jojoCap.split()

print(jojo)

## Example List
jojoList = ['Johny', 'Joseph', 'Jotaro', 'Josuke']

# returns from Jonathan to Jotaro
print(jojoList[0:3])

# returns from Jotaro up to the end
print(jojoList[2:])

# returns from the beginning up to Jotaro
print(jojoList[:3])

# changes value of a certain index
jojoList[0] = 'Jonathan'
print(jojoList[0])

# loop through the list then edit the content
count = 0
print('The Joestar family tree line: ')
for x in jojoList:
    if x == 'Jotaro':
        x = x + ' Kujo'
    elif x == 'Josuke':
        x = x + ' Higashita'
    else:
        x = x + ' Joestar'
    count = count + 1
    print('Part ' + str(count) + ': ' + x)

# User will input a value and check if it exists in the List. If not, will append
i = input('>>>> Input a Joestar member: ')
x = i.capitalize()

if x in jojoList:
    print(i, ' is already in the list.')
else:
    jojoList.append(x)
    print(x, ' succesfully added in the list.')
    print('The Joestar family tree line: ')
    print(jojoList)

# Checks the length of a List
print('> The jojoList has ' + str(len(jojoList)) + ' items.')

# remove() vs pop()
# remove() -> removes the specified item
jojoList.remove("Joseph")
print(jojoList)

# pop() -> removes the specified index
# if pop doesn't have a parameter, it automatically deleeted the last index
jojoList.pop(1)
print(jojoList)

# Copying a list by creating a list variable to reference the list that you want to copy
# + Modifying the duplicate list
list2 = list(jojo)
print(list2)
# find the index which contains the specified item. Once found, change it
list2[2] = 'WORST'
print(list2)

# JOINING LISTS
# --> by adding two lists
sidec = ['DIO', 'SPEEDWAGON', 'CAESAR', 'KAKYOIN']
casts = sidec + jojoList
print(casts)

# --> by appending list to another
casts2 = list(sidec)
for x in jojoList:
    casts2.append(x)
print(casts2)

# repeats a string and puts it in a list
y = list()
yy = 'JoJo'
y = [yy] * 4
print(y)
