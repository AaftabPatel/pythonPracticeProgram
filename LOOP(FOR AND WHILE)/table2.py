#program for table generation
n=int(input("Please enter value whose table you want:"))
print("Table of",n,"is:")
m=n*10
for i in range(n,m+1,n):
    print(n,"*",int(i/n),"=",i)
