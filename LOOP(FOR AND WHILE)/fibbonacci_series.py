print("program to print fibbonacci series till user wants")
t=int(input("PLEASE ENTER THE NUMBER OF TERMS YOU WANT TO DISPLAY"))
print("FIBO SERIES IS AS FOLLOW:")
n1=0   
n2=1
print(n1,",",n2,end="")
if t>=1:
    for i in range(1,t-1):
        fibo=n1+n2
        print(",",fibo,end="")
        n1=n2
        n2=fibo
else:
    print("0")