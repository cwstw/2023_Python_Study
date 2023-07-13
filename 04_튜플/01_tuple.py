'''
Created on 2023. 7. 13.

@author: user
'''
# tuple
#: 순서가 있는 값의 나열, 서로 다른 데이터 나열 가능,
# 튜플은 변경 불가능

#tuple은 소괄호로 묶어 생성, 나머지는 리스트와 동일
t = (1,2,3,4,5)
print(t)
print(type(t))
print(t[0])
print(len(t))
print(3 in t)
print(t[:2])
print(t[::2])
for i in t :
    print(i,end=' ')
print()

#아래의 구문은 리스트로만 만들 수 있음
print([i*3 for i in t])
print()

t1 = ()
t2 = (1,2,3)
t3 = 1,2,3
t4 = (1,)
t5 = 1,
t6 = (1)
t7 = 1

print(t1,type(t1))
print(t2,type(t2))
print(t3,type(t3))
print(t4,type(t4))
print(t5,type(t5))
print(t6,type(t6)) #int
print(t7,type(t7)) #int
print()

#튜플도 리스트처럼 연산자로 연결 가능
t1 = (1,2,3)
t2 = t1 + ('kim','park')
print(t2)

#쉼표로 연결 시 2차원 튜플 생성
t1 = (1,2,3)
t2 = t1,('kim','park')
print(t2)

#행까지 정확히 접근을 해야 true 리턴
print('kim' in t2) #False
print('kim' in t2[1]) #True
print()

#변수에 한번에 변수 정의 가능, 튜플 x
x,y,z = 1,2,3
print(x,y,z)

#두 변수의 값 바꾸기
#파이썬에서는 임시 변수를 사용하지 않을 수 있다.
x,y = y,x
print(x,y)
print()

#변수에 한번에 튜플의 값을 정의 가능 = 언패킹
t = (1,2,'hello')
print(t)
x,y,z = t
print(x,y,z)

#튜플에는 값을 넣을 수가 없다.
# t[1] = 100
#튜플을 리스트로 바꾸고 값을 삽입,
t = list(t)
t[1] = 100
#다시 리스트를 튜플로 변경
t = tuple(t)
print(t)

#서식문자에 넣을 데이터는 튜플 형태
print('id : %s, pw : %s' % ('kim','1234'))
print()

#파이썬 함수 정의
def calc(a,b):
    return a+b,a-b,a*b
#리턴값이 여러개이면 아래처럼 받을 수 있다.
x,y,z = calc(10,20)
print(x,y,z)
#하나의 변수에 여러 리턴값을 담으면 튜플로 저장된다.
x = calc(10,20)
print(x)











