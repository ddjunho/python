#202003302권준오
#
#3. 시작값과 종료값을 입력받아 홀수 합계와 갯수 구하기
#

i, hap = 0,0
num1,num2 =0,0
cnt=0
num1= int(input("시작값 : "))
시작값 : 10
num2= int(input("종료값 : "))
종료값 : 20
for i in range(num1,num2+1):
    if (i%2==1):
        hap = hap+i
        cnt+=1
print(num1,"~",num2,"홀수 합계 : ",hap,"개수 : ",cnt)
10 ~ 20 홀수 합계 :  75 개수 :  5

#
#4. 시작값과 종료값을 입력받아 그 사이의 홀수 출력
#
i=0
num1,num2 =0,0
num1= int(input("시작값 : "))
시작값 : 10
num2= int(input("종료값 : "))
종료값 : 20
for i in range(num1,num2):
    if (i%2==1):
        print(i,end=" ")

11 13 15 17 19 
