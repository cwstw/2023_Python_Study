'''
Created on 2023. 7. 14.

@author: user
'''
f = open('test.txt','w')
f.write('applebanana')
f.write('\n')
f.write('orange')
f.close()

f = open('test.txt','r')
pos = f.tell()  # 파일 포인터
print('pos:',pos)
readstr = f.read()
print('readstr:',readstr)
pos = f.tell()  # 파일 포인터
print('pos:',pos)

f.seek(5) ## 파일 포인터
readstr = f.read()
print('readstr:',readstr)

f.close()









