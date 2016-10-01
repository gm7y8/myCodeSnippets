import sys
for line in sys.stdin:
    inp=' '.join(line.split()).lower().split('|')
    mod=[]
    mod1=[]
    size=[]
    for line in inp:
       temp=(''.join(ch for ch in line.strip() if ch.isalnum() or ch==' '))
       mod.append(temp)
       size.append(len(temp))
       mod1.append(temp.replace(" ",""))
    print(mod)
    print(size)
    for i in range(0,len(mod1)):
        for j in range(0,len(mod1)):
            if mod1[i] in mod1[j] or not mod1[j].startswith(mod1[i]):
                print("yes")
            else :
                print("no")

