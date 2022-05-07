import matplotlib.pyplot as pl
l1=[1,2,3,4,5,6]
l2=[1,4,9,16,25,36]
l3=[1,8,27,64,125,216]
pl.plot(l1,l2,"r",linewidth=2,linestyle='dotted',marker='>',markeredgecolor='r')
pl.plot(l1,l3,"c",linewidth=2,linestyle='dotted',marker='>',markeredgecolor='c')
pl.xlabel("NUMBERS")
pl.ylabel("SQUARES AND CUBES")