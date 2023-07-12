'''
Created on 2023. 7. 12.

@author: user
'''
#print 후엔 자동 엔터
print('오늘은'+'즐거운'+'수요일',sep="~")
#+가 없어도 가능
print('오늘은''즐거운''수요일',sep="~")
#쉼표 구분 시 띄어쓰기, sep으로 공백에 넣을 문자 지정 가능
print('오늘은','즐거운','수요일',sep="~")

#문자열로 인식
print("12"+"34")
#숫자 연산
print(12+34)
#형변환( 자료형이 다르면 오류 발생 )
print(12+int("34"))
print(str(12)+"34")

#정수 출력
print("%d / %d = %d" % (10,3,10/3))
#실수 출력
print("%d / %d = %f" % (10,3,10/3))
print("%d / %d = %.2f" % (10,3,10/3))

#반복 출력
print("*!#" * 3)

#소수점 표시 나눗셈
print(15/6)
#소수점자리 버리는 나눗셈
print(15//6)
#나머지 연산
print(15%6)

#파이선 기본 함수, (몫, 나머지) 형태(튜플 형태)로 출력
print(divmod(15,6))

# 파이선 변수 선언 시 타입이 없음
a=10
b=20
c="abc"
#변수의 타입 반환
print(type(a))
print(type(c))

# a++, ++a 없음
a += 1
print('a:',a)

#10의 3승 연산
a = 10
a = a ** b
print('a:',a)


a = 10
#둘 다 참이면 True 반환
print((a > 0) and (a > b))
#거짓이면 False 반환
print((a > 0) and (a < b))
#not 연산자 사용
print(not((a > 0) or (a < b)))
















