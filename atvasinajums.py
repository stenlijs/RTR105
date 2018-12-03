import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

def f(x):
    return sin(x)

x=linspace(0, 4, 11)
print(x)
#y=sin(x)
y=f(x)
print(y)

legend = []

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('$sin(x)$ funkcijas un tas atvasinajumi')
plt.plot(x,y, 'k')
legend.append('$sin(x)$ funkcija')
plt.plot(x,y, 'go')
legend.append('$sin(x)$ funkcija(dazi punkti)')
deltax = x[1]-x[0]
N = len(x)

atvasinajums = []

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    atvasinajums.append(temp)
    print(atvasinajums)

plt.plot(x,atvasinajums, 'y')
legend.append('atvasinajums')

plt.plot(x, atvasinajums, 'ro')
legend.append('atvasinajums(dazi punkti)')

atvasinajums_caur_masivu = []
for i in range (N-1):
    temp = (y[i+1] - y[i]) / (x[i+1]-x[i])
    atvasinajums_caur_masivu.append(temp)
    
plt.plot(x[0:N-1], atvasinajums_caur_masivu, 'm')
legend.append('atvasinajums (izmantojot veribas no masiva)')

plt.plot(x[0:N-1], atvasinajums_caur_masivu, 'bo')
legend.append('atvasinajums (izmantojot veribas no masiva) (dazi punkti)')
#print(plt.legend.__doc__)
plt.legend(legend, loc = 3)
plt.show()
