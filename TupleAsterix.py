#Using asterix in a tuple

jojoMain = ('Jonathan', 'Joseph', 'Jotaro', 'Josuke', 'Jolynne', 'Giorno')
jojoOther = ('Dio', 'Speedwagon', 'Polnareff', 'Kakyoin', 'Avdol', 'Iggy')

#Unpack them and place them in a variable
(part1, part2, *part3) = jojoMain #In unpacking, use the variable name of the tuple

print(part1, part2, part3)


print('##########')
#Loop through the index number of a Tuple
#If you only put length, it only get its integer of how many are the values in the list
#In onrder to loop through a tuple, use a range to a length
for x in len(jojoMain):
    print(x)

print('##########')
#Adding two tuples
finalTuple = jojoMain + jojoOther #You cannot use append because tuples are immmutable
                                  #
print(finalTuple)
