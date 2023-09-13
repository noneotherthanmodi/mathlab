from math import *
def func(m,n):
    return n**m

def bij(m,n):
    if m==n:
        return factorial(n)
    else:
        return 0
    
def one_to_one(m,n):
    if m<n:
        return perm(n,m)
    else:
        return 0
    
def onto(m,n):
    sum = 0 
    if m>=n:
        for k in range(n):
            sum+= (-1)**k*comb(n,n-k)*(n-k)**m
    return sum

    
m = int(input("Enter |A|:"))
n = int(input("Enter |B|:"))
print("Number of functions from A to B: ",func(m,n))
print("Number of functions from B to A: ",func(n,m))
print("Number of one to one functions from A to B: ",one_to_one(m,n))
print("Number of one to one functions from B to A: ",one_to_one(n,m))
print("Number of onto functions from A to B: ",onto(m,n))
print("Number of onto functions from B to A: ",onto(n,m))
print("Number of bijective functions from A to B: ",bij(m,n))
print("Number of bijective functions from B to A: ",bij(n,m))