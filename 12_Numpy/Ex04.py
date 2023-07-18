'''
Created on 2023. 7. 18.

@author: user
'''
import numpy as np

list1 = [0,1,2,3,4,5,6,7,8,9]
arr1 = np.array(list1)
arange1 = np.arange(10)

print('list1:',list1)
print('arr1:',arr1)
print('arange1:',arange1)
print()

print(list1[5])
print(arr1[5])
print(arange1[5])
print()

print(list1[5:8])
print(arr1[5:8])
print(arange1[5:8])
print()

#아래처럼은 가져올 수 없다. 
# print(list1[3:2])
# print(arr1[3:2])
# print(arange1[3:2])
# print()

print(list1[3:2])
print(arr1[3::2])
print(arange1[3:2])
print()

print(list1[:2])
print(arr1[::2])
print(arange1[:2])
print()

list1[5] = 12
print('list1:',list1)

#괄호로 묶어서 넣으면 2차원 배열이 됨
list1[5] = [12]
print('list1:',list1)

#범위엔 괄호없이 넣을 수 없다.
#list1[5:8] = 33
#33하나가 범위 제일 앞 요소에 들어옴
list1[5:8] = [33]
print('list1:',list1)


arr1[5] = 12
print('arr1:',arr1)
#array는 배열 형태로 추가 불가능
#arr1[5] = [12]
#print('arr1:',arr1)

#array는 범위에 모두 33이 추가된다.
arr1[5:8] = [33]
print('arr1:',arr1)

arange1[5] = 12
print('arange1:',arange1)
#arange도 배열 형태 추가 불가능
#arange1[5] = [12]
#print('arange1:',arange1)

#arange도 범위에 모두 33이 추가된다.
arange1[5:8] = [33]
print('arange1:',arange1)


list1 = [0,1,2,3,4,5,6,7,8,9]
arr1 = np.array(list1)
arange1 = np.arange(10)

print('list1:',list1)
print('arr1:',arr1)
print('arange1:',arange1)
print()

list_slice = list1[5:8]
arr_slice = arr1[5:8]
arange_slice = arange1[5:8]

print('list_slice:',list_slice)

#list_slice를 변경해도 원본 리스트는 변경되지 않는다.
list_slice[1] = 100
print('list_slice:',list_slice)
print('list1:',list1)

#list_slice를 변경하면 원본 리스트도 변경된다.
arr_slice[1] = 100
print('arr_slice:',arr_slice)
print('arr1:',arr1)

#arange_slice 변경하면 원본 리스트도 변경된다.
arange_slice[1] = 100
print('arange_slice:',arange_slice)
print('arange1:',arange1)














