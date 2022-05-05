print("rock-paper-scissors")
c='y'
while(c=='y'):
    print("1 for rock")
    print("2 for paper")
    print("3 for scissors")
    ch=int(input("Please enter your choice:"))
    if(ch==1):
        print("Loser")
    elif(ch==2):
        print("Draw")
    elif(ch==3):
        print("Winner")
    else:
        print("Please enter correct value")
    print("do you want to continue press y to continue n to end")
    c=input("please enter y or n:")
else:
    print("thank you")
