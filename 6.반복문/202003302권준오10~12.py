#202003302권준오

#
#10. 사용자가 입력한 값 까지 홀수 합계 구하기
#
i,hap = 0,0
num = 0
num =int(input("값 : "))
while(i<=num-1):
    i+=1
    if i%2==1:
        hap += i

print("1~",num,"홀수 합계 :",hap)
1~ 10 홀수 합계 : 25

#
#11. 사용자가 입력한 값까지의 홀수 합계와 개수 구하기
#
i, hap = 0, 0
num = 0
cnt = 0
num = int(input("값 : "))
while(i<=num-1):
    i+=1
    if i%2==1:
        hap += i
        cnt+=1

print("1~",num,"홀수 합계 :",hap,"개수 :",cnt)
값 : 10
1~ 10 홀수 합계 : 25 개수 : 5
#
#12. 
#
i, hap = 0, 0
num1, num2 = 0,0
cnt = 0
num1 = int(input("시작값 : "))
num2 = int(input("종료값 : "))
while(num1<=num2-1):
    num1+=1
    if num1%2==1:
        hap += num1
        cnt+=1

print(num1,"~",num2,"홀수 합계 :",hap,"개수 :",cnt)

시작값 : 10
종료값 : 20
20 ~ 20 홀수 합계 : 75 개수 : 5


