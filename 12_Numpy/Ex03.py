'''
Created on 2023. 7. 18.

@author: user
'''
import numpy as np


a = range(5)
print('a:',a)
for i in a :
    print(i)
print()

b = np.arange(5)
print('b:',b)
for i in b :
    print(i)
print()

b = np.arange(5,10,2)
print('b:',b)
print(b.shape)
print(b.ndim)
print()

c = np.arange(6).reshape([2,3])
print('c:',c)
print(c.shape)
print(c.ndim)
print()

print('==========')

L1 = [1,2,3]
L2 = [4,5,6]

print('L1+L2:',L1+L2)

a = np.array([-1,3,2,-6])
b = np.array([3,6,1,2])

print('a+b:',a+b)

#같은 방끼리 연산
x = np.arange(3) #0 1 2
y = np.arange(10,13) #10 11 12
print('x+y:',x+y)

#배열은 사용불가
# x = np.arange(a)
# y = np.arange(b)
# print('x+y:',x+y)












