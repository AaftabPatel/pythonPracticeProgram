print("class for phone book")

class contact:
    def __init__(self,fname,lname,email,address,contact1,contact2,category):
            self.fname=fname
            self.lname=lname
            self.email=email
            self.address=address
            self.contact1=contact1
            self.contact2=contact2
            self.category=category
            
    def postdata(self):     #function for posting data
            f=open("phone.txt","a")
            pno1=str(self.contact1)
            pno2=str(self.contact2)
            p1=[self.fname,self.lname,self.email,self.address,pno1,pno2,self.category]
            for i in range(0,len(p1)):
                f.write(p1[i])
                f.write("\t")
            f.close()
            
def remove():       #function for removing data
    name=input("enter first name of the entry you want to remove:")
    l=getlist()
    if (search(name)!=-1):
        indx=l.index(name)
        for i in range(7):
            l.remove(l[indx])
        overwrite(l)
        return 1
    else:
        return 0

#function to overwrite data
def overwrite(lst):
    f=open("phone.txt","w")
    for i in range(0,len(lst)):
        f.write(lst[i])
        if(i!=len(lst)-1):
            f.write("\t")
    f.close()
        
#function to search element
def search(name):
    l=getlist()
    if (l.count(name)!=0):
        indx=l.index(name)
        return indx
    else:
        return -1
    
#function to change one value 
def change(indx,new_val):
    l=getlist()
    l.insert(indx,new_val)
    l.remove(l[indx+1])
    overwrite(l)
    
#function to update entries
def update():        
        print("what do you want to update:")
        print("1:First Name")
        print("2:Last Name")
        print("3:Email")
        print("4:Address")
        print("5:Contact1")
        print("6:Contact2")
        print("7:Category")
        ch=int(input("Make your choice:"))
        name=input("enter name of the contact you want to update:")
        if (search(name)!=-1):
            indx=search(name)
            l=getlist()
            print("name is:",l[indx])
            if(ch==1):
                new_fname=input("enter new name of the contact:")
                change(indx,new_fname)
            elif(ch==2):
                new_name=input("Enter new Last Name:")
                change(indx+1,last_name)
            elif(ch==3):
                new_email=input("Enter new Email:")
                change(indx+2,new_email)
            elif(ch==4):
                new_addr=input("Enter new Address:")
                change(indx+3,new_addr)
            elif(ch==5):
                new_con1=input("Enter new Contact1:")
                change(indx+4,new_con1)
            elif(ch==6):
                new_con2=input("Enter new Contact2:")
                change(indx+5,new_con2)
            elif(ch==7):
                new_cat=input("Enter new Category:")
                change(indx+6,new_cat)
            else:
                print("Please make correct choice!!")
        else:
            print("Name not found")
    
                
#function for geting data list
def getlist():
    f=open("phone.txt","r")
    l=f.read()
    f.close()
    l1=l.split("\t")
    return l1

#function for printing data
def getdata():
    l1=getlist()
    print("FIRST_NAME   |   LAST_NAME   |    EMAIL   |   ADDRESS   |   NUMBER1   |   NUMBER2   |   CATEGORY")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    n=1
    for i in l1:
        if(n<7):
            print("|",i,"  ",end="")
            n+=1
        else:
            print("|",i,"\n")
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
            n=1
#function for inserting data
def insert():
    num=int(input("how many entries you want:"))
    for i in range(1,num+1):
        fname1=input("Please enter the first name no.{}:".format(i))
        lname1=input("Please enter the last name no.{}:".format(i))
        email1=input("Please enter the email address no.{}:".format(i))
        addr1=input("Please enter the address no.{}:".format(i))
        no1=int(input("Please enter the first contact number no.{}:".format(i)))
        no2=int(input("Please enter the seecond contact number no.{}:".format(i)))
        cat=input("Please enter the category of contact no.:{}:".format(i))
        p=contact(fname1,lname1,email1,addr1,no1,no2,cat)
        p.postdata() 

#main program
ch="y"
while(ch=="y"):
    print("\nWELCOME TO PHONE DIRECTORY")
    print("1:select all data:")
    print("2:search one entry:")
    print("3:remove one entry:")
    print("4:insert entry:")
    print("5:update one entry:")
    print("6:Exit")
    c=input("What do want to do:")
    if(c=='1'):
        getdata()
    elif(c=='2'):
        name=input("enter first name of the entry you want to search:")        
        indx=search(name)
        l=getlist()
        if(indx==-1):
            print("value not find")
        else:
            print("value found")
            if(indx%7==0):
                for i in range(indx,indx+7):
                    print(l[i])
            else:
                indx-=indx%7
                for i in range(indx,indx+7):
                    print(l[i])
    elif(c=='3'):
        r=remove()
        if(r==1):
            print("value removed")
        else:
            print("value not find")
    elif(c=='4'):
        insert()
    elif(c=='5'):
        update()
    elif(c=='6'):
        ch="n"
        print("Thank You")
    else:
        print("Make a valid choice")


