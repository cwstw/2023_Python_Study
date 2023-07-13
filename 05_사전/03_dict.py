'''
Created on 2023. 7. 13.

@author: user
'''
from nltk.metrics import scores

student={}
while True :
    num = int(input('''번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정, 6:종료) => '''))
    if num == 1 :
        if len(student) == 0 :
            print('입력한 데이터 없음')
        else :
            print('출력')
            print('이름\t점수')
            for i,j in student.items() :
                print(i+'\t'+j)
    elif num == 2 :
        while True :
            print('입력')
            name = input('이름 : ')
            score = input('점수 : ')
            student[name] = score
            yn = input('계속? (y/n) => ')
            if yn.lower() == 'y' :
                continue
            else :
                break
    elif num == 3 :
        print('검색')
        while True :
            name = input('검색할 이름 : ')
            if name in student.keys() :
                print(name+'의 점수는 '+student[name])
                yn = input('계속? (y/n) => ')
                if yn.lower() == 'y' :
                    continue
                else :
                    break
            else :
                print('찾는 이름 없음')
    elif num == 4 :
        print('삭제')
        name = input('삭제할 이름 : ')
        if name in student.keys() :
            del student[name]
            print('삭제 완료')
        else :
            print('삭제할 이름 없음')
    elif num == 5 :
        print('수정')
        name = input('수정할 이름 : ')
        if name in student.keys() :
            score = input('수정할 점수 : ')
            student[name] = score
            print('수정 완료')
        else : 
            print('수정할 이름 없음')
    elif num == 6 :
        print('종료')
        print('프로그램을 종료합니다')
        break
    elif num < 1 and num > 6 :
        print('1부터 6 사이의 수만 입력')
    
        