
#
# 예1 : 문자열과 숫자를 활용한 예제
#


'''

print("Python")

'''
#
# 예2 : "Life is too short" 에서 'Life’단어 추출 (문자열 슬라이싱 이용)
#

'''
a = "Life is too short"
print(a[0:4])


'''
#
# 예3 : "20230315Rainy"에서 날짜와 날씨 구분 (문자열 슬라이싱 이용)
#

'''

a = "20230315Rainy"
print(a[0:4] ,"년",a[5:6] , "월", a[6:8] , "일,", "날씨 : ", a[8:])



'''
#
# 예4 : 홍길동 주민등록번호(881120‑1068234 )를 생일과 성별을 구분하여 출력 
#       (문자열 인덱싱, 슬라이싱, if 문 이용)


'''
jumin = "881120‑1068234"

print("주민번호 : ", jumin)
print("생일 : ", jumin[0:2] , "/", jumin[2:4] , "/", jumin[4:6])
if int(jumin[7]) == 1:
    print("성별 : 남")
else: print("성별 : 여")
'''
#
# # 예5: 영어 이름을 입력받아 첫글자를 모아 영어 이름 이니셜 만들어 출력(이니셜은 대문자로 변환)
#

'''
name1 = input("이름의 첫번째 글자(영어) : ")
name2 = input("이름의 두번째 글자(영어) : ")
name3 = input("이름의 세번째 글자(영어) : ")

initial=name1[0]+name2[0]+name3[0]





print("영어 이니셜 : " , initial.upper())


'''
#
# 예6 : 알파벳 소문자와 숫자 중에서 글자 3개를 랜덤으로 선택하여 패스워드 생성 프로그램 완성 
# (choice 함수 사용)
#

'''
import random

characters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"


pwd=random.choice(characters+digits)+random.choice(characters+digits)+random.choice(characters+digits)


print("생성된 패스워드: ", pwd)
'''

#
# 예7 : 결과화면을 참고하여 오류 수정
#
'''
a = [1, 2, 3]
b = str(a[2]) + "hi"
print(b)
'''

#
# 예8 : ['Life', 'is', 'too', 'short'] 리스트를 Life_is_too_short 문자열로 만들어 출력 
# (문자열의 join 함수 사용)
#
'''
list_a = ['Life', 'is', 'too', 'short']
myStr = '_'.join(list_a)
print(myStr)


'''


#
# 예9 : 주사위를 1000번 던져서 나오는 값들의 빈도 수 출력 (리스트와 난수발생 함수 사용)
#
'''
import random

counters = [0, 0, 0, 0, 0, 0]
for i in range(1000):
    if random.randint(1, 6)==1:
        counters[0]+=1
    if random.randint(1, 6)==2:
        counters[1]+=1
    if random.randint(1, 6)==3:
        counters[2]+=1
    if random.randint(1, 6)==4:
        counters[3]+=1
    if random.randint(1, 6)==5:
        counters[4]+=1
    if random.randint(1, 6)==6:
        counters[5]+=1
for i in range(6):
    print("주사위가 ", i+1, "인 경우는", counters[i])
# 주사위 1000번 던져 빈도수 저장하기


# 결과 출력하기
'''

'''
#
# 예10 : 교집합 (&, Intersection), 합집합(|, union), 차집합(-, difference) 
#

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print("집합(s1) : " ,  s1, "\n집합(s2) : ", s2)

s3= s1&s2
s4= s1.intersection(s2)

print("교집합(s3) : " ,  s3, "\n교집합(s4) : " ,  s4)

s5=s1|s2
s6=s1.union(s2)

print("합집합(s5) : " ,  s5, "\n합집합(s6) : " ,  s6)

s7=s1-s2
s8=s1.difference(s2)

print("차집합(s7) : " ,  s7, "\n차집합(s8) : " ,  s8)





#
# 예1 :교통카드 잔액 출력하기 (while 이용)
#

balance = 10000
while(balance>=0):
    print("잔액:",balance)
    balance-=1350

'''




'''


'''
#
# 예2 : 0~70 사이의 숫자 중 7으로 끝나는 숫자만 출력(while, continue, break 이용)
#

i=0
while True:
    i+=1
    for j in range(7):
        if (i-j*10)/7==1:
            print(i)
        else:continue
    if i==70:
        break







'''

'''

