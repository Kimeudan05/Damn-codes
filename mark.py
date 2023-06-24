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