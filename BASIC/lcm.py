print("program to calculate LCM")

def divi(n):
	l=[]
	if(n>=0):
		i=2
	    while(i<(n//2+1)):
	    	if (n%i==0):
	    		l.append(i)
	    		i=i
	        else:
	        	i+=1  
	elif(n==0):
	    print("zero has no divisors")
	else:
	    for i in range(n,0):
	        if (n%i==0):
	            l.append(i)
	return l
n1=int(input("Please enter first value:"))
n2=int(input("Please enter second value:"))
#n3=int(input("Please enter third value:"))
l1=divi(n1)
l2=divi(n2)
#l3=divi(n3)
print(l1)
print(l2)
l=l1+l2
print(l)
res=list(set(l))
print(res)
res=1
for i in l:
	res*=i
print("LCM of ",n1,"&",n2,"is:",res)

