#202003302권준오
#
#3. 양수/음수/0 판단
#
a=int(input("정수 : "))
정수 : 4
if a>0:
    print("정수",a,"는 양수다")
elif a==0:
    print("정수",a,"는 0이다")
else:
    print("정수",a,"는 음수다")
정수 4 는 양수다
#
#4. 3개의 정수 입력받아 가장 작은 정수 출력
#
a = int(input("정수 : "))
정수 : 10
b = int(input("정수 : "))
정수 : 2
c = int(input("정수 : "))
정수 : 39
total = 0
if a<b and a<c:
    total=a
elif b<=c and b<=a:
    total=b
elif c<=b and c<=a:
    total=c
print(a,",",b,",",c,",","중에서 가장 작은 값은 ",total)
10 , 2 , 39 , 중에서 가장 작은 값은  2

#
#5. x, y좌표 값 입력받아 사분면 출력
#
x = int(input("x값 : "))
x값 : 2
y = int(input("y값 : "))
y값 : 12
a=0
if x>=0 and y>=0:
    a=1
elif x<0 and y>=0:
    a=2
elif x<0 and y<0:
    a=3
else:
    a=4
  
if a==0:
    print("사분면의 중심")
else :
    print(a,"사분면")

1 사분면

#
#6. 건조주의보 판단
#
humidity = int(input("습도(%) : "))
습도(%) : 50
day =int(input("지속일수 : "))
지속일수 : 2
if humidity<=35 and day>=2:
    print("습도 ",humidity,"이하가 ",day,"일 이상 -> 건조주의보 알림")
else:
    print("건조주의보 알림 없음")
건조주의보 알림 없음



