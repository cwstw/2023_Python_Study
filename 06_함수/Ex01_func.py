'''
Created on 2023. 7. 14.

@author: user
'''
# abc()
def abc():
    print('하하하')
    print('호호호')
    # return
    
abc()
print('----')
print('abc():', abc())


def add(a,b):
    return a+b


print('add():', add(10,20))

result = add(1.1, 2.2)
print('result:',result)
print([10,11] + [20,21])
print(add([10,11], [20,21]))

# public void ss(){
#    
# }

def simple() :
    pass

print('simple():',simple())


def myabs(x):
    if x < 0:
        x = -x
    return x

def addabs(a,b):
    c = add(a,b)
    return myabs(c)

print(addabs(-5,-7))


def calc(x,y):
    return x+y,x-y,x*y,x/y

result = calc(13,5)
print('result:',result)
print('result[0]:',result[0])


a,b,c,d = calc(13,5)
print('a:',a)

# switch(변수, 수식){
#     case :
#     case :
#     default:
# }

def func(x):
    return{
        'a':1,
        'b':2,
        }.get(x,9)

print(func('b'))        
print(func('c'))        







    