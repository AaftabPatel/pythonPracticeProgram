print("program for operator overloading")
class test:
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2
    def __add__(self,other):
        s1=self.s1+other.s1
        s2=self.s1+other.s2
        return test(s1,s2)
    def show(self):
        print("subject 1:",self.s1)
        print("subject 2:",self.s2)
    

#main program
t1=test(65,98)
t2=test(45,65)
t3=t1+t2
print("Marks for test one are:")
t1.show()
print("Marks for test two are:")
t2.show()
print("Marks after adding are:")
t3.show()
