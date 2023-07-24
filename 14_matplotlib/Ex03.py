'''
Created on 2023. 7. 20.

@author: user
'''
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt


font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family = font_name)


x1 = [1,2,3,4]
y1 = [3,7,6,4]

x2 = [1,2,3,4]
y2 = [4,6,8,5]

plt.figure(figsize=(5,6))
plt.title('subplot 예제')
plt.xlabel('x2축')
plt.ylabel('y2축')

plt.subplot(2,2,1)
plt.plot(x1,y1,'yo-')
#yellow, 동그라미 표시

plt.subplot(2,1,2)
plt.plot(x2,y2,'r.--')
#red, diamond, 점선

















