'''
Created on 2023. 7. 18.

@author: user
'''
import numpy as np

a = 100
print('a:',a)
print(type(a))
print()

arr1 = [1,2,3,4]
print('arr1:',arr1)
print(type(arr1))
print()

arr2 = [[1,2,3,4],[5,6,7,8]]
print('arr2:',arr2)
print(type(arr2))
print(len(arr2))
print(len(arr2[0]))
print()

#numpy 모듈의 함수
b = np.array(200)
print('b:',b)
print(type(b)) #numpy.ndarray 타입
print(b.ndim) #0
print(b.shape) #()
print()

c = np.array([1,2,3])
print('c:',c)
print(type(c)) #numpy.ndarray 타입
print(c.ndim) #1 차원을 출력
print(c.shape) #(3,) 크기가 출력
print()

c1 = np.array([[1,2,3]])
print('c1:',c1)
print(type(c1)) #numpy.ndarray 타입
print(c1.ndim) #2 차원을 출력
print(c1.shape) #(1,3) 크기가 출력
print()

d = np.array([[1,2,3],[4,5,6]])
print('d:',d)
print(type(d)) #numpy.ndarray 타입
print(d.ndim) #2 차원을 출력
print(d.shape) #(2,3) 크기가 출력
print(d.shape[0]) #2
print(d.shape[1]) #3
for i in d:
    print(i)
print()










