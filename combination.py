print("program to calculate combination")
n=int(input("please enter the number of items:"))
r=int(input("please enter the number of items to be arranged:"))
def fact(n):            #function to calculate factorial
    res=1
    for i in range(2,n+1):
        res=res*i
    return res
c=fact(n)/(fact(n-r)*fact(r))
print("number of combination are:",c)
