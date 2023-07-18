'''
Created on 2023. 7. 18.

@author: user
'''
import numpy as np

a = np.array([-1,3,2,-6])
b = np.array([3,6,1,2])
c = np.array([3,6,1,2])

print(a.shape)
L1 = [1,2,3]
L2 = [4,5,6]

#기존 리스트는 연결
print('L1+L2:',L1+L2)
#print('L1*L2:',L1*L2) 불가능

#arr끼리는 연산이 된다.
print('a+b:',a+b)
print('a*b:',a*b)

#같은 방끼리 곱한 후 더한 결과
ab = np.matmul(a,b)
print(ab)

#차원 재정의
A = np.reshape(a,[2,2]) #나눠지지 않는 수로 재정의하면 오류
B = b.reshape([2,2])
print('A:',A)
print(A.shape) #(2, 2)
print(A.ndim) #2
print('B:',B)

print('A+B:\n',A+B)
print()

#행열 바꾸기
B = B.T
print('B:',B)

#1차원 배열로 정의
a = np.reshape(a,[1,4])
print('a:',a)
print(a.shape)
print(a.ndim)

#행열 변경
a = a.T
print('a:',a)
print(a.shape)
print(a.ndim)

#다시 1차원으로 재정의
a = np.reshape(a,[4])
print('a:',a)
print(a.shape)
print(a.ndim)















