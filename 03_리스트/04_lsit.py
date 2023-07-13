'''
Created on 2023. 7. 13.

@author: user
'''
from numpy import average

kor = [70,80,90]

for i in range(len(kor)) :
    print(kor[i], end=' ')
print()
for i in kor :
    print(i, end=' ')
print()
print()

#2차원 리스트
L =[['a','b'],[1,2,3]]
print(L)

#2차원 리스트 출력
#len(L) : 행의 개수
#len(L[i]) : i행의 열의 개수
for i in range(len(L)) :
    for j in range(len(L[i])) :
        print(L[i][j], end=' ')
print()
#혹은 아래 방법도 가능
for i in L :
    for j in i :
        print(j, end=' ')
print()
print()

#배열 사이에 배열 요소 끼워넣기
s = [1,2,3]
t = ['begin','end']
t[1:1] = s
print('t :',t)

#배열 사이에 배열 자체를 끼워넣기
#2차원 리스트의 형태가 된다.
#이 때 0행, 2행의 n열에는 문자열의 문자가 하나씩 들어가있다.
s = [1,2,3]
t = ['begin',s,'end']
print('t :',t)
print(t[0])
print(t[1])
print(t[2])

#insert로도 배열 자체 삽입 가능
s = [1,2,3]
t = ['begin','end']
t.insert(1, s)
print('t :',t)

print()

#3차원 리스트 (면, 행, 열)
L = [1,['a',['x','y','z'],'b','c'],7]
print(L)
print(L[0])
print(L[1])
print('L[1][1] :',L[1][1])
print('L[1][1][1] :',L[1][1][1])
print('L[1][2] :',L[1][2])
print(L[2])

print()

#0~9까지 제곱 리스트 생성
L = []
for i in range(10) :
    L.append(i**2)
print(L)

#이렇게 생략하여 생성도 가능
L2 = [i**2 for i in range(10)]
print(L2)
print()

#두 개의 1차원 리스트를 2차원 리스트로 저장
L1 = [1,2,3]
L2 = ['a','b']

for x in L1 :
    for y in L2 :
        print(x,y,end=' ')
    print()
print()

L3 = [
        [x,y] for x in L1
        for y in L2 ]
print(L3)


jumsu = [89,32,12,43,99]
#리스트 요소의 합계 구하기
print('합계 :',sum(jumsu))
#리스트 요소의 최대, 최소값
print('최대값 :',max(jumsu))
print('최소값 :',min(jumsu))
#리스트 요소의 평균 구하기
print('평균 :',sum(jumsu)/len(jumsu))
#numpy 모듈 안의 함수
print('평균 :',average(jumsu))

print()

#나열된 데이터를 반복하고 싶을 때 enumerate 사용
#start 안쓰면 0부터 시작, a에는 반복횟수 저장
for a,b in enumerate(jumsu,start=1) :
    print(a,'/',b)
print()
print()

#변수를 하나만 적으면 결과가 튜플로 출력
for a,b in enumerate(jumsu,start=1) :
    print(a)
print()

















