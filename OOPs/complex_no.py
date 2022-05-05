print("program for complex number addition and subtraction using operator overloading")
class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    #function to take complex number
    '''def inputdata(self):
        r=int(input("please enter the real part of the complex number:"))
        i=int(input("please enter the imaginary part of the complex number:"))
        self.real=r;
        self.imag=i;
'''
    #function for displaying complex number
    def displaydata(self):
        print(self.real,"+i",self.imag)

    #function to add two complex number
    def __add__(self,other):
        real=self.real+other.real
        imag=self.imag+other.imag
        return complex(real,imag)

    
    #function to subtract two complex number
    def __sub__(self,other):
        real=self.real-other.real
        imag=self.imag-other.imag
        return complex(real,imag)
    
#main program
c1=complex(1,1)
c2=complex(2,2)
#c1.inputdata()
#c2.inputdata()
print("first complex number is:")
c1.displaydata()
print("\nsecond complex number is:")
c2.displaydata()
c3=c1+c2
print("\nsum is:")
c3.displaydata()
c4=c1-c2
print("\ndiffrence is:")
c4.displaydata()

