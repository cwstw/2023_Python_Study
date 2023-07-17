'''
Created on 2023. 7. 14.

@author: user
'''
# Ex04.py
import myPkg.Ex01
result = myPkg.Ex01.add(30, 17)
print(result)
print(myPkg.Ex01.sub(30,17))

import myPkg.Ex01 as pkg
print(pkg.add(30,17))
print(pkg.sub(30,17))

# from myPkg.Ex01 import add,sub
from myPkg.Ex01 import *

c = add(30, 40)
d = sub(40, 20)
print(c)
print(d)

# 형식 정리












