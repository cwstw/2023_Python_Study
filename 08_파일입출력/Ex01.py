'''
Created on 2023. 7. 14.

@author: user
'''
import os
print(os.getcwd())

print(os.listdir('.'))
print(len(os.listdir('.')))

def filetype(f):
    print(f,":",end='')
    if os.path.isfile(f) :
        print('File')
    if os.path.isdir(f) :
        print('Directory')

flist = os.listdir('.')
print('flist:',flist)

for fname in flist :
    filetype(fname)
    
print('---------------------')    
    
    
# os.rename('a.txt', 'b.txt')
# os.rename('b.txt', 'example/c.txt')

# os.remove('a.txt')    
# os.rmdir('example')    
    
import shutil
# shutil.rmtree('example')   
    
shutil.copy('a.txt', 'b.txt') 

    
    
    
    
    
    
    
    
    
    
    
    