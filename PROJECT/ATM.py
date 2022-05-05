print("Program for ATM")

#function to get name
def get_name(no):
    l=getlist()
    i=l.index(no)
    return i

#function to check account type
def type_check(indx,type_val,l):
    if(l[indx+2]==type_val):
        return True
    else:
        False
        
#function to check PIN
def pin_check(indx,l):
    p=input("Please enter your pin:")
    if(l[indx+3]==p):
        return True
    else:
        False
#function to overwrite data
def overwrite(lst):
    f=open("Account_detail.txt","w")
    for i in range(0,len(lst)):
        f.write(lst[i])
        if(i!=len(lst)-1):
            f.write("\t")
    f.close()

#function to change one value 
def change(indx,new_val,l):
    l.insert(indx,new_val)
    l.remove(l[indx+1])
    overwrite(l)

#function for depositing money
def deposit(indx,l):
    amt=int(input("\nEnter amount to deposit:" ))
    amt+=int(l[indx+3])
    amt=str(amt)
    change(indx+3,amt,l)
    
#function for withdrawal
def withdraw(indx,l):
    amt=int(input("\nHow many Rupees to withdraw: "))
    bal=int(l[indx+3])
    if(bal-amt<0):
        print("Not Enough Money")
    else:
        amt=bal-amt
        print(amt)
        amt=str(amt)
        print(amt)
        change(indx+3,amt,l)
    
#function for displaying user info
def display(indx,l):
    print("\n\nAccount number: ",l[indx])
    print("\n\nName: ",l[indx+1])
    print("\n\nAccount type: ",l[indx+2])
    print("\n\nBalance Amount: ",l[indx+3])

#function for geting data list
def getlist():
    f=open("Account_detail.txt","r")
    l=f.read()
    f.close()
    l1=l.split("\t")
    return l1
"""
#code for adding data
f=open("Account_detail.txt","a")
l=["ac104","rahul","deposite","4444","40000"]
for i in range(0,len(l)):
    f.write(l[i])
    f.write("\t")
f.close()
"""

#main program
print("\nWELCOME TO MY ATM")
acc_no=input("Enter 5 digit Account Number:")
indx=get_name(acc_no)
l=getlist()
print("WELCOME ",l[indx+1])
print("choose your account type")
print("1:For Savings")
atype_ch=input("2:For Deposit\n:")
if(atype_ch=='1'):
   type_check(indx,"savings",l)
else:
    type_check(indx,"deposite",l)

print("What would you like to do:")
print("1:For Deposit")
c=input("2:For Withdrawal\n:")
if(c=='1'):
    deposit(indx,l)
else:
    pin_check(indx,l)
    withdraw(indx,l)

print("Would yo like to see your Account Details:")
print("1:For Yes")
detail_ch=input("2:For No\n:")
if(detail_ch=='1'):
    display(indx,l)
    print("Thank You")
else:
    print("Thank You")
