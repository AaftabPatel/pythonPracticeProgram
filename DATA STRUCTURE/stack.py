print("program to perform stack operation using list")

top= -1
def push(stk):         #function to push element
    val=int(input("please enter the value to push:"))
    global top
    top+=1
    stk.append(val)
    print("element pushed")
        
def spop(stk):             #function to pop item 
    global top
    if(top==-1):    
        print("Stack Underflow")
        return NULL
    else:
        p=stk[top]
        print(p)
        stk=stk[:-1]
        top-=1
        return p

def display(stk):       #function to dispaly stack
    global top
    if(top<0): 
        print("Stack is empty")
    else:
        print("Stack elements are:\n")
        for i in range(0,top+1):
            print(stk[i],end=" ")
stk=[]
ch="y"
while(ch=="y" or ch=="Y"):
    print("\n1) Push in stack \n 2) Pop from stack\n 3) Display stack \n 4) Exit")
    c=int(input("Enter choice: "))
    if(c==1):
        push(stk)
    elif(c==2):
        p=spop(stk)
        print("Poped element is:",p)     
    elif(c==3):
        display(stk)
    elif(c==4):
        ch="n"
    else:
        print("Invalid Choice")
else:
    print("thank you")
