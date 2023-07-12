'''
Created on 2023. 7. 12.

@author: user
'''

total = 0
i = 1
while i < 11 :
    total += i
    i += 1
print('total :',total)

#단을 입력받아 해당 단의 구구단 출력
i = 1
dan = int(input('단 입력 : '))
while i < 10 :
    #print(f'{dan} * {i} = {dan * i}') 의 형태로도 출력 가능
    print('%d * %d = %d' % (dan,i,dan*i))
    i += 1

print('===================')

#이중 while 세로 구구단 출력
i = 2
# j = 1
while i<=9 : # 2~9
    print('***',i,'단***')
    j=1
    while j<=9 :
        print(i,'*',j,'=',i*j)
        j += 1
    i += 1
    print()
    
print('===================')

#while 조건이 계속 참일 때 조건문으로 break 분기
i=1
total = 0
while True :
    total += i
    if total > 30 :
        break
    i += 1
    
print('i:',i)
print('total :',total)  




