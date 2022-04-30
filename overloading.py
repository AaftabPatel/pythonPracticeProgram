print("program for overloading")
class A:
    def write():
        print("This is class A")

class B:
    def write():
        print("This is class A")


class C(A,B):
    def write():
        print("This is class A")

#main program
item=c()
item.write()
