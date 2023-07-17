'''
Created on 2023. 7. 17.

@author: user
'''
try :
    su1 = int(input('숫자1 : '))
    su2 = int(input('숫자2 : '))
except ValueError :
    print('값이 적절하지 않습니다.')
else :
    print('덧셈 :',su1+su2)
    
print('===============')
try:
    f = open('test.txt','r',encoding='UTF-8')
except FileNotFoundError as err:
    print('파일이 존재하지 않습니다. : ',err)
else:
    print(f.read())
    f.close()
finally:
    print('finally')

print('===============')

try :
    su1 = int(input('숫자1 : '))
    su2 = int(input('숫자2 : '))
    
    if su1<0 or su2<0 :
        #에러 발생 시키기
        raise ArithmeticError('음수 입력함.')
except ArithmeticError as err:
    print('예외 발생 : ',err)
else :
    print('정상 입력')








    
