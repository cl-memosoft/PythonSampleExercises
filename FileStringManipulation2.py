#7.2 Write a program that prompts for a file name, then opens that file and reads
#through the file, looking for lines of the form:
# >>>>> X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each of the lines and compute
#the average of those values and produce an output as shown below. Do not use the sum() function
#or a variable named sum in your solution.

def get_file(x):
    count = 0 #para mabilang kung ilang characters ang meron sa line na yun
    total = 0 #i-aadd dito yung value ng bawat line na nag sstart sa 0 para maadd after ng lahat then makuha ang average

    for line in x: #mag lo-loop sa buong line
        if not line.startswith('X-DSPAM-Confidence'): continue #kapag di nag match yung line doon sa dapat nagsstart sa given na string, mag sskip siya to another line
        l = line.find('0') #kapag nag match yung line sa nag sstart sa characters sa taas, hahanapin niya naman sa line na yun yung character na 0
        num = float(line[l:]) #pag nakuha mo yung hinahanap na values, mare-read siya as string, so convert mo
                       #siya into float para magamit mo yung value niya for getting the average
        count = count + 1 #gagamit ka ng count para malaman mo kung ilang beses ka nag iterate sa buong line na nagsstart sa 0. Ba't kailangan? para mabilang mo kung ilan yung characters
                          #from 0 hanggang sa dulo
        total = total + num #eto yung part para makuha mo yung value ng float sa line at para iadd siya lahat

        #kapag nakuha na yung kung ilang characters ba sya and kung ano yung sum ng bawat characters na yun, lalabas ka na ng loop
    ave = total / count
    #idivide na para makuha mo yung average ng character na yun
    print('Average spam confidence: ', ave)


name = input('Type the file name: ')
get_file(name)
