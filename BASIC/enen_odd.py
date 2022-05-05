# program to check even odd
n=int(input("Please enter the number to check:"))
print(n%2)
if(n==0):
    print("Entered number is neither odd nor even it's zero")
elif(n%2==0):
    print("Number is Even")
else:
    print("Number is odd")
