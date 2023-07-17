'''
Created on 2023. 7. 14.

@author: user
'''
def minus(a,b):
    return a-b

print(minus(20,7))
print(minus(a=20,b=7))
print(minus(b=20,a=7))
print()

def func1(a,b=10,c=20):
    return a+b+c

print(func1(1))
print(func1(1,2))
print(func1(1,2,3))
# print(func1(1,2,3,4))
print('-----------')

def func2(*v):
    # print(v, type(v))
    for i in v :
        print(i,'/',end=' ')
    print('---------')


func2(1,2)
func2(1,2,3,4,5)
func2()
func2([1,2,3],(4,5,6))
func2("banana","apple","orange")
print('#######################')



def func3(a, *v):
    # print(v, type(v))
    for i in v :
        print(i,'/',end=' ')
    print('---------')


func3(1,2)
func3(1,2,3,4,5)
# func3()
func3([1,2,3],(4,5,6))
func3("banana","apple","orange")

print('-------------------')

tp = (10,20,30)
a,b,c = tp
print(a,b,c)


def func4(x,y,z):
    print(x,y,z)

# func4(tp)
func4(*tp)
print('-------------------')

d = {'a':1,'b':2,'c':3}
def func5(a,b,c):
    print(a,b,c)

# func5(d)
func5(*d)
func5(**d)
    
print('-------------------')
print('재귀호출')

def recursive(x):
    if x == 1:
        return 1
    return x + recursive(x-1)
        
print(recursive(10))















