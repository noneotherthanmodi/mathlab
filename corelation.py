from math import sqrt
from numpy import sum
x = [1,3,4,6,8,9,11,14]
y = [1,2,4,4,5,7,8,9]
n = len(x)
meanx = sum(x)/n
meany = sum(y)/n
devx = x-meanx
devy = y-meany
sdx = sqrt(sum([i**2 for i in devx])/n)
sdy = sqrt(sum([i**2 for i in devy])/n)
covxy = sum(devx*devy)/n
r = covxy/(sdx*sdy)

myx = r*sdy/sdx
mxy = r*sdx/sdy
from sympy import *
X1, Y2 = symbols("X1, Y2")
from pylab import *
Y1=myx*X1-myx*meanx+meany
Y1 = lambdify(X1,Y1)
X2 = mxy*Y2-mxy*meany+meanx

X2 = lambdify(Y2,X2)
X1 = linspace(0,15,100)
plot(X1,Y1(X1))
Y2 = linspace(0,15,100)
plot(Y2,X2(Y2))
scatter(x,y)
show()