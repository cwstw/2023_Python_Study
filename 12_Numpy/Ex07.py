'''
Created on 2023. 7. 18.

@author: user
'''
import numpy as np

rm = np.random.random()
print(rm) # 0<= x < 1
print(rm*10)
print(int(rm*10)+3) # 0+3~9+3 => 3~12
# print(int(np.floor(rm*10))) # 0~9

# 10~57 정수 난수
print(int(rm*48)+10) 
print()

a = np.random.permutation(10) #0~9
print(a)
print()

a = np.random.permutation(10)+3 #0+3~9+3
print(a)
print()

import random
a = random.randrange(1,10,3) # 1 4 7
print(a)
print()

print('--------------------------')

print('로또 맞추기')

# lottoNum = 1~45 정수 난수 중복안되게 6개 발생
# myNum = 내가 6번 입력 [32,2,1,11,24,31] 
#
# 1~45사이의 수 입력:32
# 1~45사이의 수 입력:32
# 이미 입력한 수입니다.
# 1~45사이의 수 입력:89
# 1~45사이의 수 입력해야합니다.
# 1~45사이의 수 입력:2
# 1~45사이의 수 입력:1
# 1~45사이의 수 입력:r
# 숫자로 입력하세요
# 1~45사이의 수 입력:11
# 1~45사이의 수 입력:24
# 1~45사이의 수 입력:31
#
# 6 : 1등
# 5 : 2등
# 4 : 3등
# 꽝

lottoNum = [] 
count=0
while len(lottoNum) != 6 :
    count += 1
    newNum = random.randrange(1,46)
    if newNum not in lottoNum :
        lottoNum.append(newNum)
        
# print(random.sample(range(1,10),6))        

print('lottoNum:',lottoNum)
# print('count:',count)
print()

count = 0
myNum =[]
while True : 
    try :
        su = int(input('1~45사이의 수 입력:'))
        if su<1 or su>45 :
            raise TypeError
        
        if su in myNum :
            raise NameError 
        
    except ValueError :
        print('숫자로 입력하세요')
            
    except TypeError :
        print('1~45사이의 수를 입력하세요')
        
    except NameError :
        print('이미 입력한 수입니다.')
    
    else :
        myNum.append(su)
        count += 1
        if count == 6:
            break

print('lottoNum:',lottoNum)
print('myNum:',myNum)

print()
ok = 0 
for i in lottoNum :
    for j in myNum :
        if i == j :
            ok += 1
            break
            
print('ok:',ok)
if ok == 6 :
    print('1등')
elif ok == 5 :
    print('2등')
elif ok == 4 :
    print('3등')
else :
    print('꽝')    










