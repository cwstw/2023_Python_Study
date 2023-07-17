'''
Created on 2023. 7. 17.

@author: user
'''
class NumBox:
    def __init__(self, num):
        self.num = num
    
    #더하기 메서드 재정의
    def __add__(self, num):
        self.num += num
        return '__add___ : '+str(self.num)

    #오른쪽에 참조변수가 있으면 radd 더하기 메서드 호출
    def __radd__(self, num):
        self.num += num
        return '__radd___ : '+str(self.num)
    
    #빼기 메서드 재정의
    def __sub__(self, num):
        self.num -= num
        return '__sub___ : '+str(self.num)
    #빼기 메서드 재정의2
    def __rsub__(self, num):
        self.num -= num
        return '__rsub___ : '+str(self.num)
        
print(1+2)
print("ab"+"cd")
print(str(12)+"ab")
print(12+int("34"))
print()

#객체 생성
su1 = NumBox(40)
print(su1.num)
print(su1.num+11)
print()

#참조변수 이름으로 연산하기
print(su1+20) # 참조변수 + 숫자 : 오버로딩
print(20+su1) # 숫자 + 참조변수

#참조변수 이름으로 연산하기
print(su1-20) # 참조변수 - 숫자 : 오버로딩
print(50-su1) # 숫자 - 참조변수





















