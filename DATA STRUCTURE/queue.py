print("program to perform queue operation using list")

top= -1
def add(que):         #function to add element
    val=int(input("please enter the value to push:"))
    global top
    top+=1
    que.append(val)
    print("element Added")
        
def remove(que):             #function to remove item 
    global top
    if(top==-1):    
        print("Stack Underflow")
        return NULL
    else:
        p=que[0]
        que.remove(p)
        top-=1
        return p

def display(que):       #function to dispaly queue
    if(top<0): 
        print("queue is empty")
    else:
        print("queue elements are:\n")
        for i in range(0,top+1):
            print(que[i],end=" ")

#main program
que=[]
ch="y"
while(ch=="y" or ch=="Y"):
    print("\n 1) Add in Queue \n 2) Remove from Queue\n 3) Display Queue \n 4) Exit")
    c=input("Enter choice: ")
    if(c=='1'):
        add(que)
    elif(c=='2'):
        p=remove(que)
        print("Removed element is:",p)     
    elif(c=='3'):
        display(que)
    elif(c=='4'):
        ch="n"
    else:
        print("Invalid Choice")
else:
    print("thank you")
