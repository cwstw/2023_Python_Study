'''
Created on 2023. 7. 12.

@author: user
'''
from conda.common._logic import TRUE

#배열 : 순서가 있는 같은 자료형을 가진 요소들의 집합
#list : 순서가 있는 값의 나열, 자료형이 서로 다를 수 있다. 리스트는 변경 가능

#여러 줄의 데이터를 정의 시 '''사용
a = '''가나다
        라마바
        아자차'''

a = 1
print(type(a))
b = TRUE
print(type(b))

#list 타입
L = [1,2,3,4,5]
print(L)
print(type(L))

#L의 요소 지정해서 출력
print(L[0])

#끝부터 셀 때는 -를 붙여 센다.
print(L[-1])

#L변수의 길이구하기
print(len(L), L.__len__())

print('============')

#반복문으로 모든 방 출력
for i in range(len(L)) :
    print(L[i], end=' ')
#혹은
for i in range(L.__len__()) :
    print(L[i], end=' ')


print()
print('============')

#리스트 형으로 데이터 출력
#1번부터 2앞까지 출력
print(L[1:2])
#1번부터 4앞까지 출력
print(L[1:4])

#끝 범위 지정 안하면 자동으로 끝까지 지정
print(L[2:])
#시작 범위도 마찬가지
print(L[:2])
#모두 출력
print(L[:])

print('============')

#list가 두 번 나열됨
print(L+L)
#list가 세 번 나열됨
print(L*3)
print('L :',L)

#리스트 요소 변경
L[1] = 10
print('L :',L)


#0~9까지 리스트 생성
# L = range(10)
# print('L :',L)
L = list(range(10))
print('L :',L)

#해당 요소가 list 안에 포함되면 True, 없으면 False
print(4 in L)
print(40 in L)

#0~9 출력
# for i in range(len(L)) :
#     print(L[i], end=' ')
#for문의 조건이 아래와 같으면 i의 값은 위치번호가 아니라 list의 요소 값을 의미
for i in L :
    print(i, end=' ')

print()

print('L[1:3] :',L[1:3])
#1번부터 3개 건너뛴 요소 출력
print('L[1::3] :',L[1::3])
#0번부터 2개씩 건너뛰어 출력
print('L[::2] :',L[::2])
#리스트 끝 부터 2개씩 건너뛰어 출력
print('L[::-2] :',L[::-2])

print('============')

L = ['apple', 'banana', 100, 200]
print(L)

#아래처럼 범위에 데이터 삽입 시 반복 가능한 형태만 삽입 가능
# L[1:1] = 9
# print(L)
#apple과 banana 사이에 9 삽입
L[1:1] = [9]
print(L)
#9가 없어지고 1~5 삽입
L[1:2] = [1,2,3,4,5]
print(L)

#문자열은 리스트 형태로 감싸주지 않으면 문자로 반복되어 저장됨
L[2:2] = 'orange'
print(L, len(L))

#해당 범위의 요소가 삭제됨
L[0:2] = []
print(L, len(L))

L[4:] = [10]
print(L, len(L))

#하나의 요소만 지우고 싶을 때 del()함수 사용
del(L[2])
print(L, len(L))

#list자체를 삭제, 출력 시 오류
del(L)
#print(L, len(L))

#1~5 리스트 생성, 합계 구하기
total = 0
for i in list(range(1,6)) :
    total += i
print("1~5의 합계 :",total)









