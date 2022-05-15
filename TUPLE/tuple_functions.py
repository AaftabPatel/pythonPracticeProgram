print("program for tuple functions")
n=int(input("Enter number of elements of tuple:"))
l=[]
for i in range(n):
    e=input("enter elements of tuple:")
    l.append(e)
t=tuple(l)
print("entered tuple is",t)
print("length of tuple is: ",len(t))
print("maximum of tuple is: ",max(t))
print("minimum of tuple is: ",min(t))
print("index of 1 in tuple is: ",t.index("1"))
print("number of 1 in of tuple is: ",t.count("1"))
