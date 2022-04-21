#program for factorial using a function
def fact(n):
    res=1
    if(n>=0):
        for i in range(2,n+1):
            res=res*i
        return res
