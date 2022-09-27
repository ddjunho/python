n=int(input())
num = n
cnt=0
while True:
    a=num//10
    b=num%10
    (a+b)%10
    num=(a+b)%10+(b*10)
    cnt+=1
    if n==num:
        print(cnt)
        break