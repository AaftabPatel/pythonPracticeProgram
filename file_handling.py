print("program for file handling")
f=open("myfirstfile.txt","w")
x=("line 1: this is line one")
f.write(x)
f.write("\nline 2: this is line two")

f.close()

f=open("myfirstfile.txt","r")
y=f.read()
print(y)
f.close()