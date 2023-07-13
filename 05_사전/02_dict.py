'''
Created on 2023. 7. 13.

@author: user
'''
p1 = {'kim':33,'park':44,'choi':55}
p2 = {'kim':77,'lee':88,'hong':99}
print(p1)
print(p1['park'])
#print(p1['jung']) 없는 키는 오류

#키에 해당하는 값 가져오기
#get으로 가져오면 없는 키도 오류대신 None으로 가져와짐
print(p1.get('park'))
print(p1.get('jung'))

if p1.get('jung') == None :
    print('jung 없음')

#update 시 키가 같은 것은 값을 덮어쓰고 없던 키는 추가
p1.update(p2)
print('p1 : ',p1)

#내용을 비우는 함수
p2.clear()
print('p2 : ',p2)

#p2자체를 삭제
del p2
#print('p2 : ',p2)

#해당 키만 삭제
del p1['park']
print('p1 : ',p1)

print()

#키 반복
for i in p1 :
    print(i)
print()

for i in p1.keys() :
    print(i)
print()

#값 반복
for i in p1.values() :
    print(i)
print()

#키와 값 반복
for i in p1.items() :
    print(i,'/',i[0],'/',i[1])
print()

for i,j in p1.items() :
    print(i,'/',j)
print()

print()

#단어와 뜻을 입력 받고 단어에 맞는 뜻을 출력
#대소문자 상관없음
#찾는 단어 없을 시 안내 출력
d={}
while True :
    word = input('단어 : ')
    if word == '' :
        break
    mean = input('뜻 : ')
    d[word.lower()] = mean
while True :
    search = input('찾는 단어 (stop 입력 시 중단) : ')
    if search.lower() == 'stop' :
        print('검색을 종료합니다.')
        break
    elif d.get(search.lower()) == None :
        print('찾는 단어가 없습니다.')
        continue
    print(search+'의 뜻은 '+d[search.lower()]+'입니다.')



