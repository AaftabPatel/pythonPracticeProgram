print("Program for selection sort")
lst=[]
n =int(input("PLEASE ENTER THE NUMBER OF ELEMENTS YOU WANT:"))
for i in range(n):
    elem=int(input("Please enter element{}:".format(i+1)))
    lst.append(elem)
print("ORIGINAL LIST IS : ",lst)
l=len(lst)

for i in range(1,l):
    v=lst[i]
    j=i-1
    while j>=0 and v<lst[j]:
        lst[j+1]=lst[j]
        j=j-1
    else:
        lst[j+1]=v
print("SORTED LIST IS : ",lst)


