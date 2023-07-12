'''
Created on 2023. 7. 12.

@author: user
'''

#입력 함수 input()
#enter 생략 시 end 값 지정
print('입력하세요 : ',end='')
a = int(input())
a = int(a)
print('a:',a)

#input 안에도 출력 문장 입력 가능
b = int(input('또 입력하세요 : '))
print('b:',b)

print(a,'더하기',b,'은(는)',int(a)+int(b),'입니다.')
print('%d 더하기 %d = %d입니다.' % (a,b,a+b))

#문자열을 기준으로 제공하는 .format() 함수
print('{} 더하기 {} 는 {} 입니다.'.format(a,b,int(a)+int(b)))
#숫자 입력 시 순서가 지정된다.
print('{1} 더하기 {0} 는 {2} 입니다.'.format(a,b,int(a)+int(b)))

#숫자에 문자열을 연결할 수 없다고 오류가 뜸
#print(a+'더하기'+b+'는'+(a+b)+'입니다.')
#숫자를 문자열로 변경하면 출력 가능
print(str(a)+' 더하기 '+str(b)+'는 '+str(a+b)+'입니다.')









