print("PROGRAM FOR LINEAR SEARCH")

def linsearch(lst1,itm1,l1):
    j=0
    while ((j<l1) and (lst1[j]!=itm1)) :
        j+=1
    
    if (j<l1):
        return j
    else:
        return "false"
 
l=int(input("PLEASE ENTER NO OF ELEMENTS OF AN LIST:"))
lst=[]

for i in range(0,l):
    e = int(input("PLEASE ENTER THE ELEMENT OF THE LIST:"))
    lst.append(e)
lst.sort()

sitm=int(input("ENTER THE ELEMENT WHICH YOU WANT TO SEARCH:"))

print("\n ENTERED LIST IS: \n",lst)

ret = linsearch(lst,sitm,l)

if (ret=="false"):
    print("SORRY ELEMENT NOT FOUND IN A LIST")
else:
    print("ELEMENT FOUND AT INDEX",ret ," AND POSITION AT",ret+1 )
        
    

    
