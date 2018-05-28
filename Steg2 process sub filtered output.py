import re
fout3 = open('outputsteg2.txt')
s3fout = open('outputsteg3.txt', 'w')
#print(fout3)
sumlist1= []
myarr = []
for line3 in fout3:
    line3 = line3.rstrip()
    #print(type(line))
    #print(len(line))
    lst1 = re.findall('\S+<', line3)

    for letter in lst1:
        #print(len(letter))
        #print(letter)
        #print(len(letter))
        #print(letter[:(len(letter)-1)])

        s3fout.write((letter[:(len(letter)-1)])+" ")
        myarr.append(letter[:(len(letter)-1)])
        #myarr.append(" ")

    #print(type(lst1))
    myarr.append(',')
    s3fout.write("\n")
    #print("\n")
    sumlist1.append(lst1)
print("Run 'Steg3 process 3td times.py'")
#print(sumlist1)
#print(myarr)
