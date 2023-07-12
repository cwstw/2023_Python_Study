'''
Created on 2023. 7. 12.

@author: user
'''

#for 변수 in 반복할 데이터 : 형태로 작성
#반복할 데이터
#: range(시작, 끝, 증가값) 시작~끝-1, 증가값만큼 증가
#: range(시작, 끝) 시작~끝-1, 무조건 1증가
#: range(끝) 0~끝-1, 무조건 1증가

#1부터 10 미만까지 3씩 증가하며 i 출력
for i in range(1,10,3) :
    print(i)

#1부터 5 미만까지 1씩 증가하며 출력
for i in range(1,5) :
    print(i)
    print('하하하')

#0부터 5 미만까지 1씩 증가하며 출력
for i in range(5) :
    print(i)

#1~10까지 합계 출력
#sum은 내장 함수의 이름이기 때문에 사용 지양
#sum = 0
total = 0
for i in range(11) :
    total+=i
print('1~10까지의 합 : ',total)
print('1~10까지의 합 : '+str(total))
print('1~10까지의 합 : {}'.format(total))

#5 4 3 2 1 출력
#감소 시엔 끝값 +1까지 출력
total = 0
for i in range(5,0,-1) :
    print(i)


#10~1 1씩 감소 짝수, 홀수 합계 구하기
even = 0
odd = 0
for i in range(10,0,-1) :
    if i % 2 == 0 :
        even += i
    else :
        odd += i
print('짝수의 합 :',even) # 10 8 6 4 2
print('홀수의 합 :',odd) # 9 7 5 3 1


print()


#break
for i in range(5) :
    #i가 2보다 크면 for 빠져나가기
    if i > 2 :
        break
    print(i)
print('for문 밖')









