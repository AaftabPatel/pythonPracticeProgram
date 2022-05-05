print("Program for profit-loss calculation")

sp=int(input("please enter the selling price:"))
cp=int(input("please enter the cost price:"))
if (sp==cp):
    print("no profit no loss")
elif(sp>cp):
    p=sp-cp;
    print("profit is made of:",p)
else:
    p=cp-sp
    print("loss is made of: %d", p)

