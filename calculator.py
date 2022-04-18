print("welcome to my calculator")

def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	if(b==0):
		return "error"
	else:
		return a/b

def mod(a,b):
	if(b==0):
		return "error"
	else:
		return a%b

def pow(a,b):
	return (a**b)

def squ(a):
	return (a*a)

def cub(a):
	return(a*a*a)

def sqr(a):
	if(a<0):
		return "error"
	else:
		return (a**(0.5))

def cbr(a):
	if(a<0):
		return "error"
	else:
		return (a**(1/3))

def int_check(s):
	l=['1','2','3','4','5','6','7','8','9','0']
	for i in range(len(s)):
		if(s[i] not in l):
			print("invalid value!!!")
			return False
		else:
			return True

def float_check(s):
	l=['1','2','3','4','5','6','7','8','9','0','.']
	for i in range(len(s)):
		if(s[i] not in l):
			print("invalid value!!!")
			return False
	else:
		return True


choice=("y")
while(choice=="y" or choice=="Y"):

	print("+: for addition")
	print("-: for subtraction")
	print("*: for multiplication")
	print("/: for division")
	print("%: for modulo")
	print("^: for power")
	print("sq: for square:")
	print("cb: for cube")
	print("sr: for square root")
	print("cr: for cube root")
	c=input("please enter your choice:")

	#ch1=int(input("enter 1 for integer or 2 for float:"))
	if(c=="+" or c=="-" or c=="*" or c=="/" or c=="%" or c=="^"):
			n1=input("please enter first value:")
			n2=input("please enter second value:")
			
			if(float_check(n1) and float_check(n2)):
				n1=float(n1)
				n2=float(n2)
			
			elif(int_check(n1) and int_check(n2)):
				n1=int(n1)
				n2=int(n2)
			
			else:
				print("please enter correct choice")
				exit()
	elif(c=="sq" or c=="cb" or c=="sqr" or c=="cbr"):
		if(ch1==1):
			n=input("please enter the value:")
			int_check(n)
			n=int(n)
		elif(ch1==2):
			n=input("please enter first value:")
			float_check(n)
			n=float(n)
		else:
			print("please enter correct choice")
			exit()
	else:
		print("please enter correct value!!!")
		exit()


	if(c=='+'):
		r1=add(n1,n2)
		print(n1,"+",n2,"=",r1)
	elif(c=='-'):
		r2=sub(n1,n2)
		print(n1,"-",n2,"=",r2)
	elif(c=='*'):
		r3=mul(n1,n2)
		print(n1,"*",n2,"=",r3)
	elif(c=='/'):
		r4=div(n1,n2)
		if(r4=="error"):
			print("division by zero!!!")
		else:
			print(n1,"/",n2,"=",r4)
	elif(c=='%'):
		r5=mod(n1,n2)
		if(r5=="error"):
			print("division by zero!!!")
		else:
			print(n1,"%",n2,"=",r5)
	elif(c=='^'):
		r6=pow(n1,n2)
		print(n1,"^",n2,"=",r6)
	elif(c=='sq'):
		r7=squ(n)
		print("square of",n,"=",r7)
	elif(c=='cb'):
		r8=cub(n)
		print("cube of",n,"=",r8)
	elif(c=='sr'):
		r9=sqr(n)
		if(r9=="error"):
			print("negative values dont have square root!!!")
		else:
			print("squre root of",n,"=",r9)
	elif(c=='cr'):
		r10=cbr(n)
		if(r10=="error"):
			print("negative values dont have cube root!!!")
		else:
			print("cube root of",n,"=",r10)
	else:
		print("please enter correct choice!!!")
	choice=input("if you want to continue press y:")
else:
	print("thank you")