'''
Created on 2023. 7. 20.

@author: user
'''
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#축에 마이너스 표시할 때 추가
plt.rcParams['axes.unicode_minus'] = False

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family = font_name)

#1~12월 강수량 정보
y1_value = (21.6, 23.6, 45.8, 77.0, 102.2, 133.3, 327.9, 348.0, 137.6, 49.3, 53.0, 24.9)
x_name=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

#1~12월 기온
y2_value = (1.6, 4.1, 10.2, 17.6, 22.8, 26.9, 28.8, 29.5, 25.6, 19.7, 11.5, 4.2)

plt.xlabel('month')
plt.ylabel('평균 강수량(mm)')
plt.title('날씨 차트')

#막대 폭 설정은 3번째 자리에
bar_width=0.5
plt.bar(x_name,y1_value,bar_width,alpha=0.5,color='g')

#다른 종류의 그래프 혼합, x축을 2개로 설정
plt.twinx()
plt.plot(x_name,y2_value,color='r',marker='.')
plt.ylabel('평균 기온($^oC$)')
plt.ylim(-40,35)

plt.show()










