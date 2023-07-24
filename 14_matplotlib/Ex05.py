'''
Created on 2023. 7. 20.

@author: user
'''
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from plotly.validators.layout.geo.projection import rotation
from pandas._libs.reshape import explode

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family = font_name)

slices = [1,2,3,4]
hobby = ['영화감상','운동','게임','공부']
cols = ['c','m','r','b']

#원형 그래프 생성, 기본 3시 방향부터 시작해서 출력됨, startang로 변경가능
plt.pie(slices,labels=hobby,colors=cols,startangle=90,shadow=True,
        explode=(0,0.2,0,0),autopct='%1.2f%%')

#범례표시, loc으로 위치 조정
plt.legend(loc=1)

plt.show()










