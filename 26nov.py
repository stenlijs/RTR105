import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import cos, linspace, sin
x=linspace(0, 7, 34)
y=cos(x)
y2=sin(x)
print(vars())


from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y2)
#plt.title('Funkcija $cos(x)$')
plt.plot(x, y, color='#FF0000')
plt.plot(x, y, 'bo')
plt.plot(x, y2, color='#0000FF')
plt.plot(x, y2, 'ro')
plt.legend(['$cos(x)$', '$sin(x)$', '$cos(x)$', 'sin(x)'])
plt.show()

