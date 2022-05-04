
print("program to print a factorial of a number using recursion:")
def fact(n):
    if(n<0):
        return ("error")
    elif (n==0 or n==1):
        return 1
    else:
        return(n*fact(n-1))
num=int(input("please enter the value till you want to calculate factorial :"))
f=fact(num)
if(f=="error"):
    print("invalid input!!!")
else:
    print("factorial of ",num," is :",f)
    
        
