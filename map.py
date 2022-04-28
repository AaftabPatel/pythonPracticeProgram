print("Program for map function")

l=[1,2,3,4,5,6,7,8]
l_even= list(filter(lambda x:x%2==0,l))
l_even2= list(map(lambda x:x*2,l_even))
print("Original list is:",l)
print("Even list is:",l_even)
print("Even list is:",l_even2)



