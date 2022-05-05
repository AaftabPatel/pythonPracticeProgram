print("Program to print all divisors of a number")
n=int(input("Please enter the number to check:"))
print("Divisors are:")
if(n>=0):
    for i in range(1,n//2):
        if (n%i==0):
            print(i)
    else:
        print(n)  
elif(n==0):
    print("zero has no divisors")
else:
    for i in range(n,0):
        if (n%i==0):
            print(i)
