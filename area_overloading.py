print("Program for area's overloading")
class area_calc:
    def area(self, *x):
        ar=0
        if(len(x)==0):
            ar="no value passed"
        elif(len(x)==1):
            ar=3.14*x[0]*x[0]
        elif(len(x)==2):
            ar=x[0]*x[1]
        elif(len(x)==3):
            ar=x[0]*x[1]*x[2]
        else:
            ar="Illegal number of inputs"
        return ar
fig=area_calc()
c="y"
while(c=="y"):
    print("Which figure area do you want")
    print("1:For Circle")
    print("2:For Square")
    print("3:For Rectangle")
    print("4:For Tringle")
    print("5:Exit")
    ch=input("Make your choice:")
    if(ch=='1'):
        r=int(input("Enter radius:"))
        print("Area of circle is:",fig.area(r),"sq. unit")
    elif(ch=='2'):
        a=int(input("Enter side:"))
        print("Area of circle is:",fig.area(a,a),"sq. unit")

    elif(ch=='3'):
        l=int(input("Enter length:"))
        b=int(input("Enter breadth:"))
        print("Area of Rectangle is:",fig.area(l,b),"sq. unit")

    elif(ch=='4'):
        b=int(input("Enter base:"))
        h=int(input("Enter height:"))
        print("Area of Triangle is:",fig.area(0.5,b,h),"sq. unit")
    elif(ch=='5'):
        c="n"
        print("Thank You")
    else:
        print("Enter correct choice!!1")
