'''
Created on 2023. 7. 17.

@author: user
'''
class Parent:
    def __init__(self):
        print('Parent 생성자')
        
    def show(self):
        print('Parent show 함수')

class Child1:
    def __init__(self):
        print('Child1 생성자')
        #해당 클래스의 생성자 호출
        Parent.__init__(self)
        
    def show(self):
        print('Child1 show 함수')
        #해당 클래스의 메서드 호출 가능
        Parent.show(self)

#괄호 안에 부모 클래스를 명시하면 Parent를 상속
class Child2(Parent):
    #init을 아예 만들어주지 않았으면 부모 생성자로 이동됨
    def __init__(self):
        print('Child2 생성자')
        #부모의 생성자를 명시하지 않으면 부모 생성자 실행 안 함
        #상속하지 않았을 때와 같이 불러올 수 있음
        #Parent.__init__(self)
        #상속받을 시 super 사용가능, super에서는 self 사용 안 함
        super().__init__()
        
    def show(self):
        print('Child2 show 함수')
        #Parent.show(self)
        super().show()

#각각 객체 생성
#상속하지 않은 클래스
p = Parent()
c1 = Child1()
p.show()
c1.show()

print('=================')

#상속한 클래스
c2 = Child2()
c2.show()



























