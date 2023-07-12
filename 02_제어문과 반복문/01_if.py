'''
Created on 2023. 7. 12.

@author: user
'''
print('if문')

su = 11
#파이선 if에서는 괄호 안써도 됨, : 입력
if su % 2 == 0 :
    #if문 안 내용이 없을  때는 pass사용해서 일단 무시 가능
    pass
    #조건이 참일 때만 출력
    print(su,'는 짝수')
    #들여쓰기(tab)으로 제어문 안 구분
    print('제어문 안쪽 입니다.')
        
#무조건 출력
print('하하하')


#else도 들여쓰기로 구분
#else if는 elif 조건 :으로 입력
if su % 2 == 0 :
    print('짝수')
    print('***')
elif su == 11 :
    print('su는 11과 같다.')
else :
    print('홀수')
    print('###')
    
#무조건 출력
print('하하하')


#학점 출력
score = int(input('점수를 입력하세요. : '))

if score >= 90 :
    print('A학점')
elif score < 90 and score >= 80 :
    print('B학점')
elif score < 80 and score >= 70 :
    print('C학점')
elif score < 70 and score >= 60 :
    print('D학점')
else :
    print('F학점')




