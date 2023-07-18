'''
Created on 2023. 7. 18.

@author: user
'''
import numpy as np

arr1 = np.array([1,2,3,4,5,6]).reshape([3,2])
print(arr1)

#arr1의 2보다 큰 수에 True를 저장
result1 = arr1 > 2
print('result1:',result1)
print()

#2보다 큰 요소들만 출력
print(arr1[arr1 > 2])

a = np.array(range(1,13)).reshape([4,3])
print(a)
print()
#1행과 2행까지의 0열의 요소 출력
result1 = a[1:3,0]
print(result1)

#1행에서 2행 중 0번째 행
result1 = a[1:3][0]
print(result1)

#1행에서 3행의 0~2열 출력
result1 = a[1:3,0:2]
print(result1)

#copy를 바꾸면 원본은 바뀌지 않는다.
acopy = a[1:3,0:2].copy()
print('acopy:\n',acopy)
print()



