#fibnoci series

def fin_even(num):
    fibn = lambda n: n if n < 2 else fibn(n-1) + fibn(n-2)  #generating fibseries using recursion 
    list=[fibn(i) for i in range(num)]   #list of fibn numbers
    return sum(filter(lambda x: x % 2==0 , list))  #filtering even terms in fib fibseries
print fin_even(10)
 
 
