print("Program for filter function")

def even(n):
    return n%2==0

l=[1,2,3,4,5,6,7,8]
l_even= list(filter(even,l))
l_odd= list(filter(lambda x:x%2!=0,l))
print("Original list is:",l)
print("Even list is:",l_even)
print("Odd list is:",l_odd) 
