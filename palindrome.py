print("program to check palindrome")
s=input("Please enter the value to check:")
rev=s[::-1]
if(s==rev):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")
