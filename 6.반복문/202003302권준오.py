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
    
