#202003302권준오

#
#16. 사람수와 나이를 입력받아 평균 나이 출력
#
i, num = 0, 0
age, tot, avg = 0, 0, 0.0
num= int(input("사람수 : "))
while (i<num):
    i+=1
    age = int(input("나이 : "))
    tot = tot + age
avg = tot/num
print("%d명의 평균 나이 %3.1f " %(num, avg), end=' ')
사람수 : 2
나이 : 20
나이 : 30
2명의 평균 나이 25.0  

#
#17. 사람수와 나이를 입력받아 평균나이와 최고령 출력
#
i, num = 0, 0
age, tot, avg = 0, 0, 0.0
max = 0
num= int(input("사람수 : "))
while (i<num):
    i+=1
    age = int(input("나이 : "))
    tot = tot + age
    if age>max:
        max=age

avg = tot/num

print("%d명의 평균 나이 %3.1f, 최고령 %d " %(num, avg, max), end=' ')
사람수 : 2
나이 : 20
나이 : 30
2명의 평균 나이 25.0, 최고령 30  
#
#18. 사람수와 나이(1~99)를 입력받아 평균 나이와 최고령, 최연소 출력
#
i, num = 0, 0
age, tot, avg = 0, 0, 0.0
max, min = 0,100
num= int(input("사람수 : "))
while (i<num):
    i+=1
    age = int(input("나이 : "))
    tot = tot + age
    if age>max:
        max=age
    if age<min:
        min=age
avg = tot/num
print("%d명의 평균 나이 %3.1f, 최고령 %d, 최연소 %d " %(num, avg, max, min), end=' ')
사람수 : 2
나이 : 12
나이 : 23
2명의 평균 나이 17.5, 최고령 23, 최연소 12  
'''
#
#19. 0을 입력할 때까지 반복 입력받아 출력
#
num = 0

while True:
    num= int(input("정수(0:입력 종료) : "))
    print("입력한 수 :", num)
    if num == 0:
        break
