#Exercise Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
print('Exercise Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1')
#This is not ideal because it can change anytime. So
def getNames(x, y):
    xChar = len(x)
    xC = int(xChar)
#x[xC-2]
    x1 = x[xC-4: xC-2]
    x2 = x[xC-2: xC+1]
    print(x1 + y + x2)


getNames('Ault', 'Kelly')
