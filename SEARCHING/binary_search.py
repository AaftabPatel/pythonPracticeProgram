print("PROGRAM FOR BINARY SEARCH")
def binsearch(lst1,itm1,l1):
    beg=0
    last=l1
    while (beg<=last):
        mid=(beg+last)//2
        if (itm1==lst1[mid]):
            return mid
        elif (itm1>lst1[mid]):
            return mid+1
        else:
            return mid-1
    else:
        return "false"
 
l=int(input("PLEASE ENTER NO OF ELEMENTS OF AN LIST:"))
lst=[]

for i in range(0,l):
    e = int(input("PLEASE ENTER THE ELEMENTs OF THE LIST:"))
    lst.append(e)
lst.sort()
sitm=int(input("ENTER THE ELEMENT WHICH YOU WANT TO SEARCH:"))
print("\n ENTERED LIST IS: \n",lst)
ret = binsearch(lst,sitm,l)

if (ret=="false"):
    print("SORRY ELEMENT NOT FOUND IN A LIST")
else:
    print("ELEMENT FOUND AT INDEX",ret ," AND POSITION ",ret+1 )
        
    

    
