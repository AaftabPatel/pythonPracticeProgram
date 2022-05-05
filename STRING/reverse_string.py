print("program to reverse string using swapping")
s=input("Plaese enter the string:")
r=""
l=len(s)
for i in range(l//2):
    s[i],s[l-i-1]=s[l-i-1],s[i]
print("reverse string is:")
print(r)
