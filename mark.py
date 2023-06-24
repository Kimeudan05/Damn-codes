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

################################### sub plot()functionDraw 6 plots:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()


#########Titles
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("MAJOR")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("SALES")

plt.suptitle("MY SHOP IN KUTUS")
plt.show()

@##########################scattering plot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

#######################################matplotlib bars
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
#height=8, plt.barh,color= "#4CAF50"

plt.bar(x, y, width=0.3,color="red")
plt.show()


######################################################histogram
import matplotlib.pyplot as plt
import numpy as np

# random numbers Example: 
# Say you ask for the height of 250 people, 
# you might end up with a histogram like this:
x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()
