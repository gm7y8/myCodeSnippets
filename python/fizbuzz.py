#fizz and buzz

def fb(i):
    out=''
    if i%3==0:
        out+="fizz"
    if i%5==0:
        out+="buzz"
    if i%3!=0 and i%5!=0:
        out=i
    return out

def fbprint(x,y):
    return [fb(i) for i in range(x,y-1,-1)]

print fbprint(100,1)

