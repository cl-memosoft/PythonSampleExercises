def get_fname(x):
    file = open(x)

    for line in file:
        line = line.rstrip()
        if not line.startswith('computers'): continue
        words = line.split()
        print(words)


get_fname('words.txt')
