'''
Created on 2023. 7. 17.

@author: user
'''
from cryptography.x509 import name

class Service:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print('self.name :',self.name)
        
        
if __name__ == '__main__' :
    s1 = Service('철수')
    s1.show()



























