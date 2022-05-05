print("Program to print factorial of a num")
n=int(input("Please enter the number whose factorial you want:"))
res=1
if(n>=0):
    for i in range(2,n+1):
        res=res*i
    print("factorial of ",n,"is:",res)
else:
    print("Please enter valid value!!")
