print("rock-paper-scissors")
import random
c='y'
p1=p2=0;
while(c=='y' or c=='Y'):
    print("1 for rock")
    print("2 for paper")
    print("3 for scissors")
    ch1=int(input("Please enter your choice:"))
    ch2=random.randint(1,3)
    if(ch1==ch2):
        print("Draw")
    elif((ch1==1 and ch2==3) or (ch1==2 and ch2==1) or (ch1==3 and ch2==2)):
        print("you are the winner")
        p1+=1
    elif((ch2==1 and ch1==3) or (ch2==2 and ch1==1) or (ch2==3 and ch1==2)):
        print("computer is the winner")
        p2+=1
    else:
        print("Please enter correct value")
    print("user points:",p1)
    print("computer points:",p2)
    c=input("if you want to continue press y else not:")
else:
    print("Thank You")
