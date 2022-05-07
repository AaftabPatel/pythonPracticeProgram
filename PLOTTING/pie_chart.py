import matplotlib.pyplot as pl
l1=[1,4,9,16,25]
l2=["Sq1","Sq2","Sq3","Sq4","Sq5"]
pl.pie(l1,labels=(l2),explode=(0.2,0,0,0.5,0))
pl.title("SQUARES")
pl.savefig("D:\\piechart1.pdf")
