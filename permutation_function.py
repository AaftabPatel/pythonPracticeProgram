print("program to calculate permutation")
n=int(input("please enter the number of items:"))
r=int(input("please enter the number of items to be arranged:"))
def fact(n):            #function to calculate factorial
    res=1
    for i in range(2,n+1):
        res=res*i
    print("factorial of ",n,"is:",res)
    return res
p=fact(n)/fact(n-r)
print("number of permutation are:",p)
