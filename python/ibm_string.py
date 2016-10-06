import sys
for line in sys.stdin:
    #print(line, end="")
    rev=line[::-1]
    #print(rev)
    lis=rev.split(" ")
    for i in lis:
        #print(i,len(i), i[len(i)-1].istitle())
        if i[len(i)-1].istitle():
            print(i[0].upper()+i[1:len(i)-1]+i[len(i)-1:len(i)].lower(),end=' ')
        else:
            print(i[0].upper()+i[1:len(i)],end=' ')
