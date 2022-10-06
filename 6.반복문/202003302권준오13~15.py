#202003302권준오

#
#13. 시작값과 종료값을 입력받아 그 사이의 홀수 출력
#
i = 0
num1, num2 = 0, 0
num1 = int(input("시작값 : "))
num2 = int(input("종료값 : "))
while(num1<=num2-1):
    num1+=1
    if num1%2==1:
        print(num1, end=" ")
시작값 : 10
종료값 : 20
11 13 15 17 19 
#
#14. 시작값과 종료값을 입력받아 그 사이의 홀수 개수와 * 로 출력
#
i, cnt = 0, 0
num1, num2 = 0, 0
num1 = int(input("시작값 : "))
num2 = int(input("종료값 : "))
start = num1
while(num1<=num2):
    num1+=1
    if num1%2==1:
        print("*", end=" ")
        cnt+=1
print("\n%d ~ %d 홀수 갯수 : %d" % (start, num2, cnt))
시작값 : 1
종료값 : 10
* * * * * 
1 ~ 10 홀수 갯수 : 5

#
#15.  3명의 나이를 입력받아 평균 아이 출력
#
i = 0
age, tot, avg = 0, 0, 0.0
while (i<3):
    i+=1
    age = int(input("나이 : "))
    tot = tot + age
avg = tot/3
print("3명의 평균 나이",avg, end=' ')
나이 : 23
나이 : 12
나이 : 34
3명의 평균 나이 23.0 

