'''
Created on 2023. 7. 13.

@author: user
'''

L = [10,20,30,40,10]

#처음 만난 해당 값의 위치 출력
#없는 값을 찾으면 에러
print(L.index(20))
print(L.index(10))

#해당 값의 개수 출력
print(L.count(10))

#요소의 위치를 뒤집는 함수
L.reverse()
print(L)

#정렬(기본 오름차순)
L.sort()
print(L)
#기본값(오름차순)
L.sort(reverse=False)
print(L)
#기본값(내림차순)
L.sort(reverse=True)
print(L)

#파이썬 기본 함수를 이용한 정렬
#이 경우 정렬을 수행한 값을 다시 리스트에 저장해주어야 함
L = sorted(L)
print(L)

#문자열 정렬 (a,b,c 순)
L =['orange','apple','grape','banana']
L.reverse()
print(L)

L.sort()
print(L)

#원래 문자열 숫자 정렬(1,2,3 순)
L = ['172','34','269','1345']
#key 속성으로 문자열 숫자를 숫자로 보고 정렬 가능
L.sort(key=int)
print('l:',L)














