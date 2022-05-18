print("program to search in tuple")
t=input("please enter the value of tuple:")
t=tuple(t)
c=input("please eneter the value whose index you want: ")
if c in t:
    co=0
    for i in t:
        if i!=c:
            co+=1
        else:
            break
    print(c,"is at index",co)
    print("in tuple",t)
else:
    print(c,"is not in ",t)    
    