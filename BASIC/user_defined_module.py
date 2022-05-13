print("program to calculate permutation using user-defined module")
import fact_func as f
n=int(input("please enter the number of items:"))
r=int(input("please enter the number of items to be arranged:"))
res1=f.fact(n)
res2=f.fact(r)
res3=f.fact(n-r)
p=res1/res2
c=res1/(res2*res3)
print("number of permutation are:",p)
print("number of combination are:",c)
