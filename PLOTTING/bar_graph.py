import matplotlib.pyplot as pl
l1=[1,2,3,4,5,6]
l2=[1,4,9,16,25,36]
pl.bar(l1,l2,width=[0.1,0.2,0.3,0.4,0.5,0.6],color=('g','r','b','c','m','k'))
pl.xlabel("NUMBERS")
pl.ylabel("SQUARES")