from math import sin, fabs
from time import sleep
def f(x):
    return sin(x)
k=0
a=1.1
b=3.2

funa = f(a)
funb = f(b)

if (funa * funb > 0.0):
    print ("dotajaa intervaalaa [%s, %s] saknju nav"%(a,b))
    sleep(1); exit()
else:
    print("dotajaa intervaalaa sakne(s) ir!")
    # definee precizitaati(delta/epsilon), ar kaadu mekleesim sakni:
    deltax = 0.01 # sashaurinaam saknes mekleeshanas robezshas:
    
    while (fabs(b-a) > deltax):
        x= (a+b)/2; funx=f(x)
        if( funa * funx < 0):
            b = x
        else:
            a=x
print("sakne ir: ", x)
print("y koordinata", sin(x))
print("iteraciju skaits ir", k)
