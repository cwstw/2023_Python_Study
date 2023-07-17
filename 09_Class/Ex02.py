'''
Created on 2023. 7. 17.

@author: user
'''
class Student :
    name = "철수"
    
    #자바와 달리 생성자의 이름이 클래스의 이름과 같지 않다
    def __init__(self,num): #생성자
        #넘어온 매개변수를 출력
        print('Student 생성자 :',num)
        #인스턴스 변수를 생성할 때는 self. 붙여 저장
        self.num = num
        
    def info(self):
        print('self.name :',self.name,self.num)

#객체 생성
#생성자를 통한 매개변수 주입 (매개변수 받는 생성자 없으면 오류)
s1 = Student(10)
s2 = Student(20)

s1.info()
s2.info()













