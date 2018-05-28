import re
#The StoryofSpaceX.en.vtt
print("Enter vtt file name :")
x = open(input())
fout = open('outputsteg2.txt', 'w')
#print(x)
sumlist= []

count = 0
for line in x:
    line = line.rstrip()
    if re.search('<c>', line):
        #print(line)
        #print("\n")
        lst1 = re.findall('\S+/', line)
        for letter in lst1:
            fout.write(letter+" ")
        fout.write("\n")
        sumlist.append(lst1)
        #print("\n")

#print("The result is \n\n\n\n")
#print(sumlist)
print("Run 'Steg2 process sub filtered output.py'")
