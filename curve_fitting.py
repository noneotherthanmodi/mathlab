from numpy import sum

x = [1,3,4,6,8,9,11,14]
y = [1,2,4,4,5,7,8,9]
n = len(x)
sy = sum(y)
sx = sum(x)
x2= [i**2 for i in x]
sx2 = sum(x2)
xy = [i*j for i,j in zip(x,y)]
sxy= sum(xy)
print("∑X=",sx,"∑Y=",sy,"∑X2=",sx2,"∑XY=",sxy)
from sympy import *
a,b,X = symbols('a,b,X')
neq1 = Eq(a*sx+n*b,sy)
neq2 = Eq(a*sx2+b*sx,sxy)
sol = solve([neq1,neq2],(a,b))
a1 = sol[a]
b1=sol[b]
from pylab import *
Y = a1*X+b1
Y=lambdify(X,Y)
X= linspace(0,16,20)
plot(X,Y(X))
scatter(x,y)
show()