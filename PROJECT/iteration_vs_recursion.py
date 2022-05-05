print("Program to write execution time for recursion vs iteration for factorial")
import time

def fact_ite(n):
    res=1
    if(n>=0):
        for i in range(2,n+1):
            res=res*i
        return res
    else:
        return 1


def fact_recur(n):
    if(n<0):
        return ("error")
    elif (n==0 or n==1):
        return 1
    else:
        return(n*fact_recur(n-1))
f=open("file1.txt","w")

for n in range(5,100,5):
    initial1=time.time()
    f1=fact_recur(n)
    print(f1,"\n")
    t1=time.time()-initial1
    print(t1)
    f2=fact_ite(n)
    print(f2)
    t2=time.time()-t1
    t1=str(t1)
    t2=str(t2)
    f.write(t1)
    f.write("\t")
    f.write(t2)
    f.write("\n")
f.close()


f=open("file1.txt","r")
d=f.read()
f.close()

l=[]
l=d.split("\n")
print("\n\n\ndata is:",l)