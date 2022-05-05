print("program for arbitarary argument")
def avg(*val):
    res=0
    for i in val:
        res+=i
    return res/len(val)
n=avg(1,2,3,4)
print("average is:",n)


#default argument=def fun(x)
#keyword argument=def fun(x=1)
#arbitrary argument=def fun(*val)
