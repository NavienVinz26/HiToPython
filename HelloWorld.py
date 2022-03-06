print('Hello,World!')

def DoubleList(x):
    Newlist = []
    for i in range (0,len(x)):
        result = x[i] * x[i]
        Newlist.append(result)
    return Newlist
print (DoubleList([1,2,3,4]))
