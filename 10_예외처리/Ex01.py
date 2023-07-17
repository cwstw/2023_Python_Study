'''
Created on 2023. 7. 17.

@author: user
'''
x = 4
y = 0
L = [1,2,3]

try :
    #4를 0으로 나누면 오류 발생
    print(x/y)
    #없는 범위의 리스트에 접근 시 오류 발생
    print(L[3])
#별칭 설정 후 출력 시 오류 상세내용 출력
except ZeroDivisionError as err:
    print('ZeroDivisionError 발생 :',err)
#처음에 발생한 오류만 예외처리 된다.
except IndexError as err:
    print('IndexError 발생 :', err)
#정확히 에러 명을 모를 때 except를 사용하여 모든 에러를 잡아준다.
#except는 except들 중 맨 아래에 작성
except :
    print('except')
    
#오류가 없을 때
else :
    print('else는 오류가 없을 때 실행') 
#finally는 무조건 수행
finally:
    print('finally')
   
#예외처리 시 예외 발생 시에도 다음 구문 정상 출력
print('예외처리 공부 중')