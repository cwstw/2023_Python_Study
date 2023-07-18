'''
Created on 2023. 7. 18.

@author: user
'''
import numpy as np

su = 2
rep_cnt = 5
result = np.repeat(su,rep_cnt)
print(result)
print(type(result))
print()

arr1 = np.array([1,2]) 
arr2 = np.array([3,4])
result = arr1 + arr2
print(result)
print()

result = np.concatenate((arr1,arr2))
print(result)
print()

arr = np.array([1.57,2.48,3.93,4.33])
print('arr:', arr)
print()

result = np.ceil(arr)
print(result)
print()

result = np.floor(arr)
print(result)
print()

result = np.round(arr)
print(result)
print()

result = np.round(arr,1)
print(result)
print()

arr2 = np.sum(arr), np.average(arr), np.mean(arr), np.min(arr) , np.max(arr)
print('arr2:',arr2)
print('arr2[0]:',arr2[0])
print()

arr1 = np.array([1.57,2.48,3.93,47.33])
arr2 = np.array([1.57,12.48,3.93,4.33])

result = np.maximum(arr1,arr2)
print("maximum result:" , result)
print()

result = np.minimum(arr1,arr2)
print('result:',result)





