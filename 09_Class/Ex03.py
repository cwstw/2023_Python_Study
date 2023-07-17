'''
Created on 2023. 7. 17.

@author: user
'''
class Bank :
    #이자율
    rate = 0.3
    
    def __init__(self, money):
        #객체가 넘기는 매개변수를 저장
        self.money = money
    
    #이자율을 적용한 금액을 다시 변수에 저장
    def save(self):
         self.money = self.money * (1 + self.rate)
    
    #변수에 저장되니 값을 출력    
    def show(self):
        print('금액 : %d' % (self.money))

b1 = Bank(10000)
b2 = Bank(20000)

b1.save()
b2.save()

b1.show()
b2.show()































