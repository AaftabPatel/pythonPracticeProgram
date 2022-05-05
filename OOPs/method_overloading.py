print("Program for method overloading")
class average:
    def avg(self, *x):
        a=0
        s=0
        if(len(x)==0):
            a="NO values provided"
        else:
            for i in x:
                s+=i
            a=s/len(x)
        return a
y=average()
print("Average is:",y.avg(12,5,7,89))
