print("program to calculate permutation")
n=int(input("please enter the number of items:"))
r=int(input("please enter the number of items to be arranged:"))
res1=res2=1
for i in range(2,n+1):
    res1=res1*i
for i in range(2,r+1):
    res2=res2*i
p=res1/res2
print("number of permutation are:",p)
