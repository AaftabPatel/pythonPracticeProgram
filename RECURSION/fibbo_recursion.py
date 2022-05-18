
print("program to print a fibonacci series ")
def fibo(n1):
    if n1==1:
        return 0
    elif n1==2:
        return 1
    else:
        return(fibo(n1-1)+fibo(n1-2))
n=int(input("please enter the number of terms till you want the series :"))
for i in range (1,n+1):
    print(fibo(i),end=',')
print('...')