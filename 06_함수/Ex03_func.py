'''
Created on 2023. 7. 14.

@author: user
'''

x=10
def func1():
    x=20
    x=x+3
    y=30
    print('x:',x,'y:',y)

func1()
print('x:',x)
# print('y:',y)
print('------------')

def func2():
    global x,a,b,c
    x=20
    x=x+3
    y=30
    print('x:',x,'y:',y)

func2()
print('x:',x)    

print('------------')

def func3(x):
    return x ** 2

print(func3(8))

# lambda 매개변수:반환값

a = lambda x : x**2
print(a(8))
# print(a)

b = lambda x,y : x+y
print(b(2,4))
   
    








