'''
Created on 2023. 7. 20.

@author: user
'''
import folium
#위치정보 시각화 라이브러리

m = folium.Map(location=[37.552270,126.980079],
               zoom_start=20)

m.save('c:/map/map1.html')

folium.Marker(location=[37.552270,126.980079],
               popup='용산도서관',
               icon=folium.Icon(icon='cloud')).add_to(m)

m.save('c:/map/map2.html')

folium.CircleMarker(location=[37.556738,126.919608],
                    popup='쌍용강북교육센터',
                    radius=50,
                    color='red',
                    fill_color='#39ac21',
                    icon=folium.Icon(icon='info_sign')).add_to(m)
m.save('c:/map/map3.html')

m = folium.Map(location=[37.5053542,127.7043419],
               zoom_start=15)

#로또판매점의 위도경도 위치
lotto = [
  {"store":"담배","loc":[37.62585944357624,127.01847823823798]},   
  {"store":"화곡본마트","loc":[37.54248103738589,126.84414659211494]},   
  {"store":"용꿈돼지꿈","loc":[37.5447438346992,126.95223862043447]},  
  {"store":"일이오마켓","loc":[37.47943673430032,126.98346178441342]},   
  {"store":"여명슈퍼마켓","loc":[37.61432815661055,127.0415039221072]},   
  {"store":"5가로또레드탑","loc":[37.570756251987575,127.00235901546226]},   
  {"store":"복권세상","loc":[35.91885025656432,128.55034430109828]},   
  {"store":"복권전문점","loc":[37.50384327747725,126.71513104367074]},   
  {"store":"인현동지하가판","loc":[37.47627910055104,126.63147671205866]},   
  {"store":"CU(광주서동점)","loc":[35.14814807640179,126.90555219336346]},   
  {"store":"지산로또방","loc":[35.148338888178,126.93203920504686]},   
  {"store":"천사로또방","loc":[37.63618838692431,127.21107884503209]},
  {"store":"오렌지통신","loc":[37.42889361993242,127.10232604117991]},   
  {"store":"여수복권방","loc":[37.418353650942116,127.12640523182601]},   
  {"store":"둘리복권방","loc":[37.34532813934063,126.73627994929885]},   
  {"store":"금성24시편의점","loc":[37.84401249737699,127.06236893072152]},   
  {"store":"GS25(청주주은점)","loc":[36.60987111587086,127.49134026856717]},   
  {"store":"장미슈퍼","loc":[36.276304155315685,126.90940713047799]},   
  {"store":"장미슈퍼","loc":[36.276304155315685,126.90940713047799]},   
  {"store":"아이24(수송점)","loc":[35.970108052787594,126.7189421934312]},   
  {"store":"탑로또","loc":[34.87844231008963,128.62803523643754]} 
]

#markercluster : 모이는 곳은 한번에 개수로 표시됨
from folium.plugins import MarkerCluster
marker_cluster = MarkerCluster().add_to(m)

for i in range(len(lotto)) : #0~20
    folium.Marker(location=lotto[i]['loc'],
                  popup=lotto[i]['store'],
                  icon=folium.Icon(color='red',icon='ok')).add_to(marker_cluster)
                  
m.save('c:/map/map4.html')

print('지도 생성됨')






