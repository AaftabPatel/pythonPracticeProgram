import numpy as np
import matplotlib.pyplot as pl
month=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
zon=["north","south","east","west","central"]
ln=[140.0,130.0,130.0,190.0,160.0,200.0,150.0,170.0,190.0,170.0,150.0,120.0]
ls=[160.0,200.0,130.0,200.0,200.0,170.0,110.0,160.0,130.0,140.0,170.0,200.0]
le=[140.0,180.0,150.0,170.0,190.0,140.0,170.0,180.0,190.0,150.0,140.0,170.0]
lw=[180.0,150.0,200.0,120.0,180.0,140.0,110.0,130.0,150.0,190.0,110.0,140.0]
lc=[110.0,160.0,130.0,110.0,120.0,170.0,130.0,200.0,150.0,160.0,170.0,130.0]
l=[ln,ls,le,lw,lc]
n=np.arange(12)
pl.bar(n+0.0,l[0],width=0.15)
pl.bar(n+0.15,l[1],width=0.15)
pl.bar(n+0.30,l[2],width=0.15)
pl.bar(n+0.45,l[3],width=0.15)
pl.bar(n+0.60,l[4],width=0.15)
pl.xlabel(month)
pl.ylabel(zon)
pl.savefig("d:\\bar.pdf")