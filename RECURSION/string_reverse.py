("program  to print a string backword")
def rev(s1,n):
    if n>0:
        print(s[n], end='')
        rev(s1,n-1)
    elif n==0:
        print(s1[0])
s=input("please enter the string to reverse :")
rev(s,len(s)-1)