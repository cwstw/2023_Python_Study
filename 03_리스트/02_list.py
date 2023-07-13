'''
Created on 2023. 7. 13.

@author: user
'''
#복습
#1~10 리스트 생성, 출력
L = list(range(1,11))
print(L)
#3과 4 사이에 11추가
L[3:3] = [11]
print(L)
#4 대신 12 추가
L[4:5] = [12]
print(L)

print()

#맨 뒤에는 추가 가능
print(len(L))
L[11:11] = [13]
print(L)

print()

#맨 뒤에 요소를 추가하는 함수
L.append(14)
print(L)

#2번째에 요소 끼워넣기
#insert(index, object)
L.insert(2, 15)
print(L)

#2번째 요소 꺼내기(삭제)
L.pop(2)
print(L)

#가장 먼저 만난 2의 값을 가진 요소 삭제
L.remove(2)
print(L)

print()

#반복해서 5번 숫자 입력 후 리스트 생성, 출력
L=[]
for i in range(5) :
    L.append(int(input('숫자 입력 : ')))
print(L)

#리스트끼리의 연산(=연결의 개념)
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print(L3)

L=[]
for i in range(5) :
    L += [int(input('숫자 입력 : '))]
print(L)



















