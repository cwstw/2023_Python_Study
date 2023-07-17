'''
Created on 2023. 7. 14.

@author: user
'''
import math
print(math.pi)

result = math.factorial(5)
print(result)

from math import *
print(factorial(5))

from math import factorial as f
print(f(5))

print(max(3,2,12,89,6))
print(min(3,2,12,89,6))
print(abs(-3))
print(pow(2,3))
print(round(2.3))
print(round(2.7))
print(round(-2.3))
print(round(-2.7))
print(round(3.14567,3))
print(round(98513.14568,-3))

print('------------------')


import datetime
print(datetime.datetime.now())

from datetime import *
now = datetime.now()
print('now:',now)
print(type(now))
print('연:',now.year)
print('월:',now.month)
print('일:',now.day)
print('시:',now.hour)
print('분:',now.minute)
print('초:',now.second)
print("%d-%d-%d" % (now.year,now.month,now.day))
# 오늘날짜의 요일 알아보기
print(datetime.weekday(date(now.year,now.month,now.day)))
print('요일:',now.today()) 
print('요일:',now.today().weekday()) 

def func(x):
    return{
        0:'월요일',
        1:'화요일',
        2:'수요일',
        3:'목요일',
        4:'금요일',
        5:'토요일',
        # 6:'일요일'
        }.get(x, '잘못된 숫자')
now2 = datetime.weekday(date(now.year,now.month,now.day))
print(func(now2))
    
print(func(now.today().weekday()))





