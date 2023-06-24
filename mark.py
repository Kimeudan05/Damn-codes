@############adding fonts

import matplotlib.pyplot as dan
import numpy as carol

x=carol.array([2,4,6,8])
y=carol.array([4,8,12,16])

font1 = {'family':'serif','color':'blue','size':20}
font2={'family':'serif', 'color':"red"}

dan.xlabel("Carols trials")
dan.title("Masila against Carol trials", fontdict=font1 ,loc='left')
dan.ylabel("daniel trials" ,fontdict=font2)

dan.plot(x,y ,marker="X")

dan.show()

##########################grid addition in pythopn matplotlib

import matplotlib.pyplot as masila
import numpy as np

x=np.array([2,3,4,5])
y=np.array([5,6,7,8])

masila.plot(x,y ,marker="*")
masila.grid(color = 'green', linestyle = '--', linewidth = 0.5)

masila.show()
