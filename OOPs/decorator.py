from div_support import *
print("program for decorator")

def smart_div(func):        #decorator
    def inner(p,q):
        if(p<q):
            p,q=q,p
        return func(p,q)
    return inner

a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=div(a,b)
div1=smart_div(div)
d=div1(a,b)
print("value of c is:",c)
print("value of d is:",d)
