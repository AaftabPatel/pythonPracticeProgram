import matplotlib.pyplot as pl
import numpy as np
x=np.arange(0.,10,0.1)
y=np.sin(x)
z=np.cos(x)
pl.plot(y,'r',linestyle='dashed')
pl.title("sin and cos graph")
pl.plot(z,'c')