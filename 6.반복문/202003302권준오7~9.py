#202003302권준오

#
#7. 사람수와 나이를 입력받아 평균 나이 출력
#
i, num = 0,0
age=0
tot = []

avg=0
num = int(input("사람수 : "))
사람수 : 3
for i in range(1,num+1):
    age=int(input("나이 : "))
    tot.append(age)
    
나이 : 21
나이 : 32
나이 : 22
avg = sum(tot)/len(tot)
print("3명의 평균 나이 : ",avg,end=" ")
3명의 평균 나이 :  25.0 

#
#8. 사람수와 나이를 입력받아 평균나이와 최고령 출력
#
i, num = 0,0
age=0
tot = []
avg=0
max1 = 0
num = int(input("사람수 : "))
for i in range(1,num+1):
    age=int(input("나이 : "))
    tot.append(age)
avg = sum(tot)/len(tot)
max1 =max(tot)
print("3명의 평균 나이 : ",avg, "최고령", max1)

3명의 평균 나이 :  22.666666666666668 최고령 24
#
#9. 사람수와 나이(1~99)를 입력받아 평균 나이와 최고령 출력
#
i, num = 0,0
age=0
tot = []
avg=0
max_age = 0
min_age = 0
num = int(input("사람수 : "))
for i in range(1,num+1):
    age=int(input("나이 : "))
    tot.append(age)
avg = sum(tot)/len(tot)
max_age =max(tot)
min_age = min(tot)
if age<=99 and age>=1:
    print("3명의 평균 나이 : ",avg, "최고령", max_age, "최소령",min_age)
else:
    print("나이 규격에 맞지 않습니다.")
    
사람수 : 3
나이 : 23
나이 : 34
나이 : 54
3명의 평균 나이 :  37.0 최고령 54 최소령 23
