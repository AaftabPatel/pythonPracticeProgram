a=input("Enter the first number:")
b=input("Enter the second number:")
if(a.isdigit() and b.isdigit()):
    a,b=int(a),int(b)
    if(a>b):
        n=a
    else:
        n=b
    while(1):
        if(n%a==0 and n%b==0):
            print("LCM is:",n)
            break
        n+=1
else:
    print("please enter correct value!!!")