#Write a Python program to read first n lines of a file

def get_file(x):
    fname = open(x)

    for line in fname:
        if not line.contains('\n'):
            print(line)
        break


file = 'words.txt'
get_file(file)
