#program for table generation
n=int(input("Please enter value whose table you want:"))
print("Table of",n,"is:")
for i in range(1,11):
    print(i,"*",n,"=",i*n)
