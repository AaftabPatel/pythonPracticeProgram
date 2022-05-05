print("A PROGRAM TO CHECK PRIME NUMBER")
n=int(input("PLEASE ENTER NUMBER YOU WANT TO CHECK:"))
if(n>=2):
    for i in range(2,n//2+1):
         if n%i==0:
            print(n,"IS NOT A PRIME NUMBER")
            break
    else:
        print(n,"IS A PRIME NUMBER")    
else:
    print("Invalid Value!!!")
