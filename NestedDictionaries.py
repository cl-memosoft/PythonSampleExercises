# Creating Dictionary that contains Dictionary

#jojoMain is a dictionary that contains 3 another dictionaries
#which are jojo1, jojo2, jojo3
jojoMain = {
    'jojo1' : {
        'name' : 'Jonathan Joestar',
        'part' : 1
    },
    'jojo2' : {
        'name' : 'Joseph Joestar',
        'part' : 2
    },
    'jojo3' : {
        'name' : 'Jotaro Kujo',
        'part' : 3
    },
    'jojo4' : {
        'name' : 'Josuke Higashita',
        'part' : 4
    }
}

print(jojoMain)

# Adding 4 existing dictionaries to a Dictionary
jojo1 = {
    'name' : 'Jonathan Joestar',
    'part' : 1
}
jojo2 = {
    'name' : 'Joseph Joestar',
    'part' : 2
}
jojo3 = {
    'name' : 'Jotaro Kujo',
    'part' : 3
}
jojo4 = {
    'name' : 'Josuke Higashita',
    'part' : 4
}

## This is the main dicionary where you will add the 3 existing dictionaries
jojoChars = {
    'jojo1' : jojo1, #the string 'jojo1' is the key and you're passing the jojo1 dictionary as a dictionary value
    'jojo2' : jojo2, #use colon in assining a dictionary as a value
    'jojo3' : jojo3,
    'jojo4' : jojo4
}
print(jojoChars)
