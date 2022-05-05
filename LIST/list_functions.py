print("A PROGRAM TO PERFORM ALL LIST FUNCTIONS:")
n=int(input("PLEASE ENTER NUMBERS OF ELEMENTS OF THE LIST:"))
l1=[]
for i in range(n): 
    e=input("PLEASE ENTER ELEMENTS OF LIST:")
    l1.append(e)
print("list after append is: ",l1)
print("index of 1 is: ",l1.index('1'))
n=int(input("PLEASE ENTER NUMBERS OF ELEMENTS OF THE LIST:"))
l2=[]
for i in range(n): 
    e=input("PLEASE ENTER ELEMENTS OF SECOND LIST:")
    l2.append(e)

print("list 1 after extent is: ",l1.extend(l2),l1)
print("list 1 after insrting 9 at index 3  is: ",l1.insert(3,9),l1)
print("list 1 after poping 9 is: ",l1.pop(0),l1)
print("list 1 after removing 9 is: ",l1.remove(9),l1)
print("list 1 counted members are : ",l1.count(1),l1)
print("list 1 after reversing is: ",l1.reverse(),l1)
print("list 1 after sorting is: ",l1.sort(),l1)
print("list 1 after clear is: ",l1.clear(),l1)
