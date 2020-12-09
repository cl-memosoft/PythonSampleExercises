#Using Range and Len Functions

#[] - Add friends name until done
#[] - Print friends name
#[] -

def friends_list(name):
    count = 0
    friends = []

    while True:
        friends.append(name)

    if name == 'done':
        for friend in range(friends):
            print(friends[friend], "")
            break


fName = input('Enter list of names. If done, type done. ')
lowerfn = fName.lower()

while True:
    friends_list(lowerfn)
