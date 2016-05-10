#list concatination

list1=[1 ,2, 3 ]
list2=['a' ,'b' ,'c']

def list_concat( l1 ,l2 ):
    return [x for t in map(None, l1, l2) for x in t if x]

print list_concat( list1, list2)
