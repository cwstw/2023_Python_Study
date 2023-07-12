'''
Created on 2023. 7. 12.

@author: user
'''

#음수 입력 시 입력 정지
#평균 10의 자리의 수 만큼 *출력
count = 0
total = 0
while True :
    count += 1 #반복횟수
    score = int(input('점수 입력 : '))
    total += score
    if score < 0 :
        break
print('반복 횟수 :',count)
print('합계 :',total)
print('평균1 : %.2f' % (total/count))
print('평균2 : {:.2f}'.format(total/count))

avg = total/count

for i in range(int(avg/10)) :
    print('*',end='')
    
#print('*' * int(avg/10))로도 출력 가능

