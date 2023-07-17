'''
Created on 2023. 7. 17.

@author: user
'''
from Library.plugins import position

class Person:
    #값이 들어오지 않으면 age는 90
    def __init__(self,name, age=90):
        self.name = name
        self.age = age
    #ToString처럼 주소 리턴
    def __str__(self):
        #재정의 가능
        return'Person %s %d' % (self.name, self.age)
        
p1 = Person('홍길동',30)
p2 = Person('아이유')

print(p1.name) #홍길동
print(p1.age) #30
#참조변수 출력 시 자동으로 str 수행
print('p1 :',p1)

print(p2.name) #아이유
print(p2.age) #90
print('p2 :',p2)

print('====================')

class Employee(Person):
    #변수를 4개 받아오는 생성자
    def __init__(self, name, age, position, salary):
        #부모 생성자 호출해서 name과 age를 넘겨줌
        super().__init__(name, age)
        self.position = position
        self.salary = salary
    
    #출력 시에도 부모의 str 메서드를 가져와 사용
    def __str__(self):
        return '사원명/나이: %s / 직급 : %s / 급여 : %d' % (super().__str__(),self.position,self.salary)
     
#객체 생성
e1 = Employee('태연',40,'대리',200)
e2 = Employee('효연',50,'과장',300)

#출력
print(e1.name)
print(e1.age)
print(e1.position)
print(e1.salary)
print('e1 :',e1)

print(e2.name)
print(e2.age)
print(e2.position)
print(e2.salary)
print('e2 :',e2)










