print("Area of figure using polymorphism")
def area(r):
    if check(r):
        r=float(r)
        if(r>=0):
            print("area of circle is",3.14*(r**2))
        else:
            print("radius cannot be negative")
    else:
        print("invalid value!!!")

def area(a):
    check(a)
    if(a>=0):
        print("area of square is: ",a*a)
    else:
        print("side cannot be negative")
def area(l,b):
    check(l)
    check(b)
    if(l>=0 and b>=0):
        print("area of square is: ",l*b)
    else:
        print("length cannot be negative")
print("1:for circle")
print("2:for square")
print("3:for rectangle")
ch=int(input("choose figure whose area you want:"))
if(ch==1):
    r=input("please enter the radius of circle: ")
    area(r)
elif(ch==2):
    l=float(input("please enter the length of rectangle: "))
    b=float(input("please enter the breadth of rectangle: "))
    area(l,b)
elif(ch==3):
    a=float(input("please enter the side of square: "))
    area(a)
else:
    print("please choce correct choice!!")
