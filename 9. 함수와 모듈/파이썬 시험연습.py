#202003302권준오
'''
#1,2 홀수 합계, 개수
i,hap = 0,0
num =0
cnt = 0
num = int(input("값:"))
for i in range(num+1):
    if i%2 != 0:
        hap+=i
        cnt+=1
print(hap,"  개수:",cnt)

#3,4 홀수입력 합계, 개수
#
i,hap = 0,0
num1,num2 =0,0
cnt = 0
num1 = int(input("시작값:"))
num2 = int(input("종료값:"))
for i in range(num1,num2+1):
    if i%2 != 0:
        hap+=i
        cnt+=1
        print(i,end = " ")
print(hap,"  개수:",cnt)

#while 홀수입력 합계, 개수
i,hap = 0,0
num1,num2 =0,0
cnt = 0
num1 = int(input("시작값:"))
num2 = int(input("종료값:"))
while(num1<=num2):
    if num1%2 != 0:
        hap+=num1
        cnt+=1
        print(num1,end = " ")
    num1+=1

print(hap,"  개수:",cnt)

#리스트 초기화,수정,연결,반복,길이,추가,조건출력
list = [10,20,30,40,50]
print(list)
list[4] = 100
print("수정:",list)
list_a = [10,20]
list_b = [30,40,50]
print("a,b합:",list_a+list_b)
print(list_a+list_a)
print(len(list_a))
list_a.append(100)
print(list_a)
list_a.insert(1,-100)
print(list_a)
num = [1,123,23,345,5467,2]
for i in num:
    if i>=100:
        print(i)

#딕셔너리 생성,길이,추가,수정,삭제,get(),in
cafe = {1:'아메리카노',2:'카푸치노'}
print(cafe)
cafe[3]='스무디'
print(cafe)
print(len(cafe))
del cafe[2]
print(cafe)
print(cafe.get(1))
print(cafe.get(2))
print(2 in cafe)
        
#핸드폰 예제
contacts ={}
while(True):
    i = input("이름:")
    if i == "":
        break
    contacts[i] = input("핸드폰 번호:")
print("연락처:",contacts)
i=input("찾는 이름:")
if contacts.get(i)==None:
    print("없음")
else: print(contacts[i])
'''
#문자열 예제
'''
mystr= input("입력단어:")
if len(mystr)>2:
    print(mystr,end='ing')
else:print(mystr)

if mystr.endswith('ing') == True:
    print(mystr,end='ly')
else: print(mystr,end='ing')
'''
mystr='봄 여름 가을 겨울'
print(mystr)
print(mystr.replace('가을','fall'))
print(mystr)
#함수와 모듈
#
