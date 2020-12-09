#Exercise Question 1: Given a string of odd length greater 7, return a string made of the middle three chars of a given String
print('Exercise Question 1: Given a string of odd length greater 7, return a string made of the middle three chars of a given String')

def get_word(x):
    strCnt = len(x)
    strDiv = strCnt / 2
    ans = int(strDiv)

    final = x[ans - 1: ans + 2]
    print(final)


word = input('Enter a word: ')
get_word(word)
