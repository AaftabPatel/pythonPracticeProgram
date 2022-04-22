print("program to make a function for area of figures according to users choice:")

def check(s):
    l=['1','2','3','4','5','6','7','8','9','0','.']
    for i in range(len(s)):
        if(s[i] not in l):
            print("invalid value!!!")
            return False
        else:
            return True

def aoc():
    r=input("please enter the radius of circle: ")
    if check(r):
        r=float(r)
        if(r>=0):
            print("area of circle is",3.14*(r**2))
        else:
            print("radius cannot be negative")
    else:
        print("invalid value!!!")

def aos():
    a=float(input("please enter the side of square: "))
    check(a)
    if(a>=0):
        print("area of square is: ",a*a)
    else:
        print("side cannot be negative")
def aor():
    l=float(input("please enter the length of rectangle: "))
    b=float(input("please enter the breadth of rectangle: "))
    check(l)
    check(b)
    if(l>=0 and b>=0):
        print("area of square is: ",l*b)
    else:
        print("length cannot be negative")
def aot():
    b=float(input("please enter the base of right angled triangle: "))
    h=float(input("please enter the height of right angledtriangle: "))
    check(b)
    check(h)
    if(l>=0 and b>=0):
        print("area of square is: ",0.5*b*h)
    else:
        print("side cannot be negative")

print("enter: \n c: for circle \n r: for rectabgle \n s: for square \n t: for triangle")
n=input("please enter your choice:")
i=n.lower()

if i=='c':
    aoc()
elif i=='s':
    aos()
elif i=='r':
    aor()
elif i=='t':
    aot()
else:
    print("please enter right choice")
