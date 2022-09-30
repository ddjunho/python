#202003302권준오

#
#5. 시작값과 종료값을 입력받아 그 사이의 홀수 갯수와 *로 출력
#
i= 0
num1, num2 = 0,0
cnt=0
num1= int(input("시작값 : "))
시작값 : 1
num2= int(input("종료값 : "))
종료값 : 10
for i in range(num1,num2):
    if (i%2==1):
        print("* ",end=" ")
        cnt +=1

*  *  *  *  *  
print(num1,"~",num2,"홀수 개수 : ",cnt)
1 ~ 10 홀수 개수 :  5

#
#6. 3명의 나이를 입력받아 평균나이 출력
#
i=0
tot = []
age=0
for i in range(1,4):
    age=int(input("나이 : "))
    tot.append(age)

나이 : 21
나이 : 23
나이 : 22
avg = sum(tot)/len(tot)
print("3명의 평균 나이 : ",avg,end=" ")
3명의 평균 나이 :  23.2 