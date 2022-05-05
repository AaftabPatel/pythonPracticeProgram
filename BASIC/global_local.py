print("program for local and global variable")
c=1
def plus():
	global c
	c=1
	c+=1
def minus():
	global c
	c-=1
print("count is:",c)
plus()
minus()
minus()
print("count is:",c)