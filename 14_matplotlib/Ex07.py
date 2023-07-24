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

#기호로 구분된 대용량 csv 읽어오기
mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드',
            'TCS하이패스구분코드', '1종교통량', '2종교통량',
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량', 'Noname']
filename = 'capital_area.csv'
#쉼표 구분이 아니면 보통 table 사용
#names=mycolumn :인덱스 지정
df = pd.read_table(filename,sep='|',names=mycolumn)
print('df:\n',df)

#영업소 코드가 같은 것끼리 그룹
df = df.groupby('영업소코드')[['1종교통량', '2종교통량', '3종교통량', '4종교통량', '5종교통량', '6종교통량']].mean()
print()

plt.xlabel('영업소코드')
plt.ylabel('교통량')
plt.title('교통량 평균')

df.plot.bar()

plt.show()










