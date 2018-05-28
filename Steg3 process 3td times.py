import re
import os
fout3 = open('outputsteg3.txt')
s4fout = open('outputsteg4.txt', 'w')
myfile1="outputsteg2.txt"
myfile2="outputsteg3.txt"
myarr3 = []
myarrTest = []
#print(fout3)
for line4 in fout3:
    line4 = line4.rstrip()
    #print(line4)
    #print(type(line4))
    lst1 = re.findall('\S+', line4)
    for letter in lst1:
        #print(len(letter))
        myarrTest.append(letter)

        if (letter[0:1] == '<'):
            #print("Bug found")
            #print(letter[15:])
            myarr3.append(letter[15:])
            s4fout.write((letter[15:])+" ")

        elif (letter[(len(letter)-1):(len(letter))] == '>'):
            #print("hello C M ", letter[(len(letter)-1):(len(letter))])
            myarr3.append((letter[ :(len(letter)-4)]))
            s4fout.write((letter[ :(len(letter)-4)])+" ")
        else:
            myarr3.append(letter)
            s4fout.write(letter+" ")


    s4fout.write("\n ")


#print(myarr3)
#print(myarrTest)


try:
    os.remove(myfile1)
    os.remove(myfile2)
except:
    print("Already removed")

print("outputsteg4.txt Exported successfully")
