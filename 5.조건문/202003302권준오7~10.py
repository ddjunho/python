# 202003302 권준오
#
#7. 강풍주의보 판단
#
wind_speed1 = int(input("육상 풍속(m/h) : "))
육상 풍속(m/h) : 10
wind_speed2 = int(input("순간 풍속(m/h) : "))
순간 풍속(m/h) : 40
if wind_speed1>=14 and wind_speed2>=20:
    print("육상 풍속(m/h)이 ",wind_speed1,"이상 또는 순간 풍속(m/h)이 ",wind_speed2,"이상 -> 강풍주의보 알림")
else:
    print("강풍주의보 알림 없음")

    
강풍주의보 알림 없음

#
#8. 감자칩 가격과 구입 개수 입력받아 계산.
#
강풍주의보 알림 없음
price = int(input("감자칩 가격 : "))
감자칩 가격 : 1500
cnt = int(input("구입 갯수 : "))
구입 갯수 : 10
price1 = 0
if cnt >= 10:
    price1=price*9/10
print(price,"원 짜리 감자칩 ",cnt,"개 구입 -> 총 금액은 ",price1,"원")
1500 원 짜리 감자칩  10 개 구입 -> 총 금액은  13500.0 원

#
#9. 감자칩 가격과 구입 개수 입력받아 계산.
#
price = int(input("감자칩 가격 : "))
감자칩 가격 : 1500
cnt = int(input("구입 갯수 : "))
구입 갯수 : 20
price1 = 0
if cnt >= 10:
    price1=price*9/10
elif cnt >= 20:
    price1=price*8/10

print(price,"원 짜리 감자칩 ",cnt,"개 구입 -> 총 금액은 ",price1*cnt,"원")
1500 원 짜리 감자칩  20 개 구입 -> 총 금액은  27000.0 원

#
#10. 자격증 시험(엑셀, 엑세스) 합격 여부 프로그램
#
excel = int(input("엑셀 점수:"))
엑셀 점수:40
access=int(input("엑세스 점수:"))
엑세스 점수:95
total=""
if excel<50 and access<60:
    total="과락으로 불합격"
else:
    if excel+access/2<60:
        total="불합격"
    else:
        total="합격"
print("엑셀 점수 : ",excel,"점, 엑세스 점수 : ",access,"점\n총점 : ",excel+access,"점, 평균 : ",excel+access/2,"점\n결과 : ",total)
엑셀 점수 :  40 점, 엑세스 점수 :  95 점
총점 :  135 점, 평균 :  87.5 점
결과 :  합격

