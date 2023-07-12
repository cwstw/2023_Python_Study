'''
Created on 2023. 7. 12.

@author: user
'''


#이중 for문
for i in range(1,4) : #1 2 3
    for j in range(6,8) : #6 7
        print(i,j)
    print('========')
print('###')

#*을 한 개씩 늘려 5개까지 출력
#이중 for문 이용
for i in range(5) :
    for j in range(i+1) :
        print('*',end='')
    print()
#* 사용
for i in range(6) :
    print('*'*i)