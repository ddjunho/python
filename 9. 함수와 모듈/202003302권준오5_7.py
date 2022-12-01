#202003302권준오
'''
#
# 4-5 : 함수(calc_triangle) 이용하여 삼각형 넓이 구하기
#
def calc_triangle(val1, val2):
    return val1*val2/2
val1 = 5
val2 = 10
result = calc_triangle(val1, val2)
print("밑변 %d, 높이 %d 인 삼각형 넓이 %f" %(val1, val2, result))
#
# 4-6 : 함수 (calc_snack) 이용하여 새우깡 1개 가격과 구입 갯수 입력받아 총 구입금액 계산
#
def calc_snack():
    price=int(input("새우깡 가격은?"))
    taget = int(input("몇개 구입?"))
    print("새우깡 1개의 가격은 ",price,",",taget,",개 구입, 총 구입금액은 ",price*taget)
calc_snack()
#
# 4-7 : 함수(calc_time) 이용하여 초 -> 시, 분, 초로 계산하기
#
'''
tot_sec=0
hour = 0
minute = 0
second = 0
def calc_time(tot_sec):
    hour = tot_sec // 3600
    minute = tot_sec - hour*3600-60
    second  = tot_sec // 60-60
    print("%d 초 -> %d시간, %d분, %d초" %(tot_sec,hour, minute, second))
calc_time(3661)

