'''
Created on 2023. 7. 12.

@author: user
'''

season = 'suMmEr'
print(season)
#대문자 변환
print(season.upper())
#소문자 변환
print(season.lower())
#첫 글자만 대문자
print(season.capitalize())

#전부 대문자면 true
print(season.isupper())

#파이선은 문자열 비교 시에도 == 사용
#결과는 30
if season == 'summer' :
    a = 10
elif season == 'winter' :
    a = 20
else :
    a = 30
print('a :',a)


#결과는 10
if season.lower() == 'summer' :
    a = 10
elif season == 'winter' :
    a = 20
else :
    a = 30
print('a :',a)








































