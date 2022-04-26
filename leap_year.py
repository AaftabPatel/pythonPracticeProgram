print("program for leap year")
y=int(input("Please enter the year to check:"))
if(y%400==0):
    print(y," is a leap year")
elif(y%100==0):
    print(y," is a leap year")
elif(y%4==0):
    print(y," is a leap year")
else:
    print(y," is not a leap year")
