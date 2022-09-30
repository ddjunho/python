#202003302권준오
#
#1. 사용자가 입력한 값까지의 홀수 합계 구하기
#
i, hap = 0,0
num=0
num=int(input("값: "))
값: 10

for i in range(1,num+1,2):
    hap+=i

print("1 ~",num,"합계 : ",hap)
1 ~ 10 합계 :  25

#
#2. 사용자가 입력한 값까지의 홀수 합계와 갯수 구하기
#
i,hap=0,0
num =0
cnt=0
num=int(input("값 : "))
값 : 10
for i in range(1,num+1):
    if (i%2==1):
        hap = hap+i
        cnt+=1
print("1 ~",num,"홀수합계 : ",hap,"개수 : ",cnt)
1 ~ 10 홀수합계 :  25 개수 :  5