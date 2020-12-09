#This is for github purposes only.
#I will add this to see changes

# Program that matches a string that has an a followed by zero or more b's
import re

def text_match(txt):
    patterns = 'ab*?'
    if re.search(patterns, txt):
        return('Found a match!')
    else:
        return('Not matched!')


print(text_match('ac'))
print(text_match('abc'))
print(text_match('abbc'))
print(text_match('vnbc'))


# Program that checks that a string contains only a certain set of characters
def isAllowed(string):
    x = re.compile(r'[a-zA-Z0-9.]')
    string = x.search(string)
    return not bool(string)

print(isAllowed('ABCDEFabcdef123450'))
print(isAllowed('*^%%&^$$'))


# Program that matches a string that has an a followed by one or more b's
def match_text(text):
    patterns = 'ab?'
    if re.search(patterns, text):
        return('Found a match!')
    else:
        return('Not matched!')


print(match_text('ac'))
print(match_text('abc'))
print(match_text('abbc'))
