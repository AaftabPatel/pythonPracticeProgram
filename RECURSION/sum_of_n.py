
print("program to print sum of n numbers")
def add(n):
    if n==1:
        return 1
    else:
        return(n+add(n-1))
last=int(input("please enter the value till you want to add :"))
s=add(last)
print("sum of n numbers is :",s)