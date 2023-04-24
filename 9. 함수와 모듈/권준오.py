#############################################################
## 2023년 1학기 파이썬 심화 프로그래밍 직무수행능력평가 1차 (주간A) ##
## 학번 :  202003302     이름 : 권준오                        ##
#############################################################

# 1(5). 학번을 입력받아 입학년도를 출력하는 프로그램
'''
num = input("학번은?")
print("입학년도는 ",num[0:4],"이군요")
'''

# 2(5). 동전을 100번 던져 앞면과 뒷면이 나온 횟수를 출력하는 프로그램
'''
import random

a, b = 0, 0 # 동전의 앞면(a)과 뒷면(b)횟수를 저장하는 변수

# 코드 완성
for i in range(100):
    i = random.randint(0, 1)
    if i == 0:
        a+=1
    else:
        b+=1

print("앞면 ", a, "번, 뒷면 ", b, "번")

# 3(10). 가로와 세로의 길이를 입력받아 사각형 넓이 계산하여 출력
'''
'''
# 함수명 : calc_rectangle
def calc_rectangle(x,y):
    return x*y



##
# 가로와 세로 길이 입력 받기
x = int(input("가로 : "))
y = int(input("세로 : "))
result = calc_rectangle(x,y)
print("가로 : %d, 세로 : %d, 사각형 넓이 : %d " % (x,y,result))
'''

# 4(10). 사각형 넓이 계산하여 출력

# 클래스 Rectangle 정의
class Rectangle:
    x, y = 0, 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def calc_rectangle(self):
        return self.x*self.y
    def print(self):
        print("가로 : %d, 세로 : %d, 사각형 넓이 : %d"%(self.x, self.y,self.calc_rectangle()))
    def setXY(self, x=0, y=0):
        self.x = x
        self.y = y



## 메인 코드 부분 ##
myRec1 = Rectangle(1,2)
myRec1.calc_rectangle()
myRec1.print()
myRec1.setXY(3,4)
myRec1.calc_rectangle()
myRec1.print()
