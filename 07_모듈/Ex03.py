'''
Created on 2023. 7. 14.

@author: user
'''
# Ex03.py
import Ex01
Ex01.abc()
Ex01.xyz()
 
import Ex01 as e
e.abc()
e.xyz()


# from Ex01 import abc,xyz
from Ex01 import *
abc()
xyz()

print('---------------')
import Ex02 
Ex02.display()


import Ex02 as E2
E2.display()

from Ex02 import display
display()

from Ex02 import *
display()



