from math import *
print("H0 = Good fit")
print("H1 = Not good fit")
x = [0,1,2,3,4]
f = [5,29,36,25,5]
ΣOi = sum(f)
n=len(x)-1
p = float(input("Enter probability of success: "))
q = 1-p
px = [comb(n,i)*p**i*q**(n-1) for i in x]
Ei = [ΣOi*i for i in px]
ΣEi = sum(Ei)
print("Ei = ",end="")
for i in Ei:
    print(i,end="  ")

print("∑Oi=",ΣOi,"   ∑Ei= ",ΣEi)
flag = [(f[i]-Ei[i])**2/Ei[i] for i in range(len(f))]

x2 = sum(flag)
print("x2 = ",x2)
df = n
x2tab = float(input("Enter tabulated value of x2: "))
if x2<=x2tab:
    print("Accept the null hypothesis")
else:
    print("Reject the Null hypothesis")


