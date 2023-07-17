'''
Created on 2023. 7. 14.

@author: user
'''
# 3 * 1 = 3
# 3 * 9 = 27
for i in range(1,10) :
    print(3,'*',i,'=',3*i)
    
print('---------------------------------')    
# gugudan.txt
dan = 3
f = open('gugudan.txt','w')
for i in range(1,10) : 
    f.write('%d * %d = %d' % (dan, i, dan*i) + '\n')
f.close()    
    
print('---------readline()------------------------')    
# gugudan.txt
f = open('gugudan.txt','r')
line = f.readline();
print('line:',line)
f.seek(0)
while True:
    line = f.readline();
    if line == '' :
        break
    print(line,end='')

f.close()

print('--------readlines()----------------------')    
f = open('gugudan.txt','r')
lines = f.readlines()
print('lines:',lines)

for line in lines:
    print(line, end='')

f.close()    
    
print('-----------read()--------------------')    
f = open('gugudan.txt','r')
readstr = f.read()
print('readstr:',readstr)
f.close()    
    
    
    
    