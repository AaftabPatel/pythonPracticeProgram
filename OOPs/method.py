print("Program for methods")

class student:
    institution="IIPS"
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def show(self):
        print("values are:",self.a,self.b)

    @classmethod
    def info(self):
        print("class belongs to:",self.institution)

    @staticmethod
    def about():
        print("this class holds data about student and their institute")

#main function
s1=student(80,90)
s2=student(78,98)
s1.show()
s2.show()
print("institute is:",s1.institution)
student.info()
s2.about()

