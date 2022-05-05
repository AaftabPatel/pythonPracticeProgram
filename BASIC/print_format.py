#program for table generation
n=int(input("Please enter value whose table you want:"))
print("Table of",n,"is:")
m=n*10
count=1
for i in range(n,m+1,n):
    print("{}*{}={}".format(n,count,i))
    count+=1
    
