'''
Created on 2023. 7. 17.

@author: user
'''
class Tiger:
    def jump(self):
        print('호랑이 jump')
    
    def cry(self):
        print('호랑이 어흥~')

class Lion:
    def bite(self):
        print('사자 bite')
    
    def cry(self):
        print('사자 으르렁~')

#다중 상속 가능
class Liger(Tiger,Lion):
    def play(self):
        print('라이거와 놀기')

l = Liger()
l.play()
l.jump()
#다중 상속받은 부모들이 같은 이름의 함수를 가지고 있을 때,
#먼저 상속받은 함수를 수행
l.cry()
l.bite()

















