
print("program  to print a is to the power b")
def power(a,b):
    if b==0:
        return 1
    else :
        return(a*power(a,b-1))
n=int(input("please enter the base number :"))
r=int(input("raised to the power of :"))
res=power(n,r)
print(n,"raised to the power of",r,"is",res)