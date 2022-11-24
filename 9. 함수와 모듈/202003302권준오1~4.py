#202003302권준오

#
# 4-1 : 함수(calc_kmTom) 이용하여 km -> m 로 변환하기
#
'''
def calc_kmTom(km) :
    m = 1000*km
    print(km,"km를 m로 변환하면 ",m)
    return km
calc_kmTom(1)

#
# 4-2 : 함수(calc_circle) 이용하여 원 넓이와 둘레 구하기
#
import math
def calc_circle(r) :
    area = r**2*math.pi
    range = 2*r*math.pi
    print("반지름이 ",r,"인 원의 면적은 ",area,", 둘레는 ",range)

#
# 4-3 : 함수(calc_rectangle) 이용하여 사각형 넓이 구하기
#
def calc_rectangle(x,y):
    area=x*y
    print("가로",x,"세로",y,"인 사각형의 넓이",area)
    
calc_rectangle(10,20)
'''
#
# 4-4 : 함수(calc_seconds) 이용하여 시간을 초로 환산하기
#
def calc_seconds(t,m,s):
    seconds=3600*t+60*m+s
    print(t,"시간,",m,"분,",s,"초 -> ",seconds)
calc_seconds(1,1,1)
