'''
num = int(input("숫자 :"))
if num <20 and num >10:
    print(num)

num = int(input("숫자 :"))
if num >20 or num <10:
    print(num)
    
temp = int(input("온도 :"))
if temp < 0:
    state="얼음"
else :
    state="기체"
print(state)

a = 67
b = 5
print("최대", int(a/b), "에게 나누어 주고", a%b)

sum = 0
for i in range(10, 0 ,-2):
    sum = sum +1
print("sum :",sum)

sum = 0
while (sum<5):
    sum+=1
print("sum :",sum)
'''
sum=0
i = 10
while (i>0):
    i -= 2
    sum += 1
print(sum)
