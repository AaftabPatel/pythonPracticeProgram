print("Program for reduce function")
from functools import reduce 

l=[1,2,3,4,5,6,7,8]
print("Original list is:",l)
s= reduce(lambda x,y:x+y ,l)
print("Sum is:",s)


