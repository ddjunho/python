import folium
from folium.plugins import HeatMap
import pandas as pd
# 승하차인원CSV 파일읽어오기
metro_people= pd.read_csv('seoul-metro-2021.logs.csv')
# 지하철역정보CSV 파일읽어오기
station_info= pd.read_csv('seoul-metro-station-info.csv')
# 승하차인원그룹화하여더하기
station_sum = metro_people.groupby("station_code").sum()
# 승하차 인원 데이터 상세 정보 확인하기
station_info = station_info[['station.code', 'geo.latitude','geo.longitude']]
# 색인 변경하기
station_info = station_info.set_index('station.code')

# 데이터 셋 합치기
joined_data = station_sum.join(station_info)

 #승차용 서울 지도 만들기
seoul_in = folium.Map(location=[37.55, 126.98], zoom_start = 12)

HeatMap(data = joined_data[['geo.latitude', 'geo.longitude','people_in']]).add_to(seoul_in)
# 승차지도 확인하기
seoul_in.save('./seoul_in.html')

# 하차용 서울 지도 만들기
seoul_out = folium.Map(location=[37.55, 126.98], zoom_start = 12)
# 히트맵 플러그인 지도에 승차인원 추가하기
HeatMap(data = joined_data[['geo.latitude',
'geo.longitude','people_out']]).add_to(seoul_out)
# 하차지도 확인하기
seoul_out.save('./seoul_out.html')
morning_data=metro_people[pd.to_datetime(metro_people.timestamp).dt.hour<9]
evening_data=metro_people[pd.to_datetime(metro_people.timestamp).dt.hour>17]
morning_station_sum = morning_data.groupby('station_code').sum()
evening_station_sum = evening_data.groupby('station_code').sum()
morning_joined_data = morning_station_sum.join(station_info)
evening_joined_data = evening_station_sum.join(station_info)

morning_seoul_in = folium.Map(location=[37.55,126.98], zoom_start=12)
HeatMap(data=morning_joined_data[['geo.latitude', 'geo.longitude','people_in']]).add_to(morning_seoul_in)
morning_seoul_in.save('./morning_seoul_in.html')

morning_seoul_out = folium.Map(location=[37.55,126.98], zoom_start=12)
HeatMap(data=morning_joined_data[['geo.latitude', 'geo.longitude','people_out']]).add_to(morning_seoul_out)
morning_seoul_out.save('./morning_seoul_out.html')

evening_seoul_in = folium.Map(location=[37.55, 126.98], zoom_start = 12)
HeatMap(data=evening_joined_data[['geo.latitude', 'geo.longitude','people_in']]).add_to(evening_seoul_in)
evening_seoul_in.save('./evening_seoul_in.html')

evening_seoul_out = folium.Map(location=[37.55, 126.98], zoom_start = 12)
HeatMap(data=evening_joined_data[['geo.latitude', 'geo.longitude','people_out']]).add_to(evening_seoul_out)
evening_seoul_out.save('./evening_seoul_out.html')