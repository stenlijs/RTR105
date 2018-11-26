import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace
x=linspace(0,4,11)
y=sin(x)
y1=x
#y2=x-x*x*x/(1*2*3)
y2 = y1-x**33(1*2*3)
#y3=x-x*x*x/(1*2*3) + x*x*x*x*x/(1*2*3*4*5)
y3= y2 + y**5/(1*2*3*4*5)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('funkcija $sin(x)$')
plt.plot(x, y, 'bo')
plt.plot(x, y, color = '##00FF00')
plt.show()

