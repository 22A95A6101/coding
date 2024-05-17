import math-->math.sqrt()
import math as M-->M.sqrt()
from math import *-->sqrt()
def add(a,b):
    res = a+b
    return  res
def sub(a,b):
    res = a-b
    return  res
def mul(a,b):
    res = a*b
    return  res
def div(a,b):
    res = a/b
    return  res
def flr_div(a,b):
    res = a//b
    return  res
def mod(a,b):
    res = a%b
    return  res
def power(a,b):
    res = a**b
    return  res




a,b = map(int,input().split())
res1= add(a,b)
res2= sub(a,b)
res3= mul(a,b)
res4= div(a,b)
res5= flr_div(a,b)
res6= mod(a,b)
res7= power(a,b)
print("add:",res1)
print("sub:",res2)
print("mul:",res3)
print("div:",res4)
print("floordiv:",res5)
print("module:",res6)
print("power:",res7)

