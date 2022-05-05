#program to check greater of three
n1=int(input("Please enter first number:"))
n2=int(input("Please enter second number:"))
n3=int(input("Please enter third number:"))
if(n1==n2==n3):
    print("All are same")
elif((n1>n2) and (n1>n3)):
    print("n1:",n1,"is the greater than n2:",n2,"& n3:",n3)
elif((n2>n1) and (n2>n3)):
    print("n2:",n2,"is the greater than n1:",n1,"& n3:",n3)
elif((n3>n1) and (n3>n2)):
    print("n3:",n3,"is the greater than n1:",n1,"& n2:",n2)
elif(n1==n2):
    if(n1>n3):
        print("n1:",n1,"is equal to n2:",n2,"& greater than n3:",n3)
    else:
        print("n3:",n3,"is greater than n1:",n1,"& n2:",n2)
elif(n1==n3):
    if(n1>n2):
        print("n1:",n1,"is equal to n3:",n3,"& greater than n2:",n2)
    else:
        print("n2:",n2,"is greater than n1:",n1,"& n3:",n3)
elif(n2==n3):
    if(n2>n1):
        print("n2:",n2,"is equal to n3:",n3,"& greater than n1:",n1)
    else:
        print("n1:",n1,"is greater than n2:",n2,"& n3:",n3)
