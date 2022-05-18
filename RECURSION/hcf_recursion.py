
print("program to compute hcf of two number")
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
n1=int(input("please enter the first value :"))
n2=int(input("please enter the second value :"))
d=hcf(n1,n2)
print("HCF of",n1,"&",n2,"is :",d)