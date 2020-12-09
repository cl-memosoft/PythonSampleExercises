name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()

for line in handle:
    line = line.rstrip()

    if not 'From ' in line:
        continue

    line = line.split()
    time = line[5] #Gets the 5th index of the list
    hour = time[:2] #Slices the up to but not including the 2
    d[hour] = d.get(hour, 0) + 1 #Creates a dictionary with 'hour' as key and assigns a count

for k, v in sorted(d.items()): #Creates a list of tuples and sorts it
	print(k, v)
