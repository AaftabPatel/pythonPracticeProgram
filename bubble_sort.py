print("program for bubble sort")
n =int(input("PLEASE ENTER THE NUMBER OF ELEMENTS YOU WANT:"))
lst=[]
for i in range(n):
    elem=int(input("Please enter element{}:".format(i+1)))
    lst.append(elem)
print("ORIGINAL LIST IS : ",lst)
l=len(lst)
for i in range(l):
    for j in range (0,l-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print("SORTED LIST IS : ",lst)            
