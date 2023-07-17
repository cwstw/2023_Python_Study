'''
Created on 2023. 7. 17.

@author: user
'''
class Person :
    #여러 객체에서 공통으로 사용 가능한 변수 (=static)
    lastname = '김'
    
    #class안의 함수에는 self 매개변수가 꼭 필요하다.
    def setname(self, name):
        print('self :',self)
        #fullname에 lastname과 매개변수로 받아온 name을 이어 저장
        self.fullname = self.lastname + name
        return self.fullname
  
#객체 생성      
p1 = Person()
p2 = Person()
#각 객체에는 객체의 주소가 들어옴
print('p1 :',p1)
print('p2 :',p2)

#변수 사용, 김 출력
print(p1.lastname)
print(p2.lastname)
print(Person.lastname)

#객체 주소 출력됨, 메서드는 각각의 객체마다 가지고 있음
#아무것도 넣지 않으면 주소가 넘어감
f1 = p1.setname('연아')
f2 = p2.setname('보검')

print(f1)
print(f2)
# fullname은 공통 변수가 아니기 때문에 오류 print(Person.fullname)


#객체를 요소로 갖는 리스트 생성
L =[p1,p2]
print(L[0])
print(L[1])
#반복해서 해당 객체의 변수 출력
for i in L :
    print(i.fullname)

























