'''
Created on 2023. 7. 13.

@author: user
'''

#사전의 정의
#자바의 map과 유사하다.
d = {'one':'hana','two':'dul','three':'set'}
print(d)
print(type(d))

#key값을 이용해서 값을 찾을 수 있다.
#값으로는 검색 불가능 print(d['dul'])
print(d['two'])

#키의 값 바꾸기
d['one'] = 1
print(d)

#없는 키의 값을 수정하면 새로 생성된다.
d['four'] = 'net'
print(d)

print(len(d))
#키의 길이를 출력 시 키의 값의 문자열 길이를 반환
print(len(d['four']))

#키로만 포함하는 요소를 검색할 수 있다.
print('one' in d) #True
print('dul' in d) #False

#키들만 출력되는 함수
print(d.keys())
#값들만 출력되는 함수
print(d.values())

#만약 값이 포함되는 지 검색하고 싶으면 d.values() 사용
print('dul' in d.values()) #True

#키와 값이 튜플로 묶여서 리스트로 출력
print(d.items())

print()

d={}
w1 = 'Hello' #5
w2 = 'World~' #6

d[w1] = len(w1)
d[w2] = len(w2)
print(d)

#사전 함수를 사용한 생성
d = dict()
print(d)
d = dict(one=1, two=2)
print(d)

#리스트를 사전으로 바꾸는 방식으로도 가능
d = dict([['one',1],['two',2]])
print(d)

#이름, 점수 입력, 그냥 입력 없이 엔터치면 반복 중단
#이름과 점수로 사전 만들기
#값들만 가지고 합계 생성

d = {}
total = 0
while True :
    name = input('이름 입력 : ')
    if name =='' :
        break
    jumsu = int(input('점수 입력 : '))
    d[name] = jumsu
    total += d[name]
print(d)
print(d.items())
#items를 이용한 출력
for i,j in d.items() :
    print('이름 :',i,'점수:',j)





