print("rock-paper-scissors")
c='y'
while(c=='y'):
    print("1 for rock")
    print("2 for paper")
    print("3 for scissors")
    ch1=int(input("Please enter your choice user1:"))
    ch2=int(input("Please enter your choice user2:"))
    if(ch1==ch2):
        print("Draw")
    elif((ch1==1 and ch2==3) or (ch1==2 and ch2==1) or (ch1==3 and ch2==2)):
        print("user1 is the winner")
    elif((ch2==1 and ch1==3) or (ch2==2 and ch1==1) or (ch2==3 and ch1==2)):
        print("user 2 is the winner")
    else:
        print("Please enter correct value")
    print("do you want to continue press y to continue n to end")
    c=input("please enter y or n:")
else:
    print("thank you")
