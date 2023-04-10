# # 예1 : km  m 로 변환하는 프로그램(1)
#
# ## KmToM 클래스 선언 부분 ##
# class KmToM :
#     km = 0
#     m = 0
#
#
#
#
# ## 메인 코드 부분 ##
# myKm = KmToM()   # 인스턴스 myKm 생성
#
# __________________          # myKm의 km를 5로 변경
#
# myKm.calc_km()      # 메소드 호출(계산)
#
#
# print(__________________________________________________________)
#


# 예2 : km  m 로 변환하는 프로그램(2)

## 클래스 선언 부분 ##
# class KmToM :
#     km = 0
#     m = 0
#     def calc_km(self):
#         self.m = 1000*self.km
#     def show_result(self):
#         return print(self.km,"km는 ", self.m,"m")
#
#
# ## 메인 코드 부분 ##
# myKm = KmToM()
# myKm.km = 5
#
# myKm.calc_km()       # 메소드 호출(계산)
# myKm.show_result() # 메소드 호출(결과 출력)


# 예3 : km  m 로 변환하는 프로그램(3)

## 클래스 선언 부분 ##
# class KmToM :
#     km = 0
#     m = 0
#     def input_km(self):
#         km = int(input("km? :"))
#         self.km = km
#     def calc_km(self):
#         self.m = 1000*self.km
#     def show_result(self):
#         return print(self.km,"km는 ", self.m,"m")
#
#
# ## 메인 코드 부분 ##
# myKm = KmToM()
#
# myKm.input_km()    #  메소드 호출(값 입력받기)
# myKm.calc_km()      # 메소드 호출(계산)
# myKm.show_result() # 메소드 호출(결과 출력)

'''
# 예4 : 동전(Coin) 클래스 (1)

import random

## 클래스 선언 부분 ##
class Coin :
    face = 0
   # 동전 던지기 : 0 혹은 1
    def flip(self):
        self.face = random.randint(0, 1)
   # 결과 출력 : 0이면 동전 앞면, 1이면 동전 뒷면 
    def show_face(self):
        print("동전",end=" ")
        if self.face==0:
            print("앞면")
        else:
            print("뒷면")
  
## 메인 코드 부분 ##
myCoin = Coin()
myCoin.flip()
myCoin.show_face()


# 예5: 동전(Coin) 클래스 (2)

import random

## 클래스 선언 부분 ##
class Coin :
    face = 0

## 메인 코드 부분 ##
myCoin = Coin()

cnt_front, cnt_back = 0, 0  # 동전 앞면과 뒷면 개수 저장 변수
# 동전 100번 던져서 앞면 혹은 뒷면 개수 세기
for i in range(100):
    face = random.randint(0, 1)
    if face == 1:
        cnt_front += 1
    else:
        cnt_back += 1

print("100번 던진 결과 앞면은 %d번, 뒷면은 %d번 나옴" %(cnt_front, cnt_back))


# 예6 : 동전(Coin) 클래스 (3)

import random

## 클래스 선언 부분 ##
class Coin :
    face = 0

    # 생성자, 동전 앞면 혹은 뒷면으로 초기화
    def __init__(self):
        self.face = 0
    def flip(self) : self.face = random.randint(0, 1)
    def show_face(self) : 
        if (self.face == 0) : print("동전 앞면")
        else : print("동전 뒷면")

## 메인 코드 부분 ##
myCoin = Coin()
myCoin.show_face()

myCoin.flip()
myCoin.show_face()
'''

# 예7: 동전(Coin) 클래스 (4)

import random

## 클래스 선언 부분 ##
class Coin :
    face = 0
    cnt_front = 0
    cnt_back = 0
    def __init__(self):
        self.face = 0
        self.cnt_front = 0
        self.cnt_back = 0
    def face_count(self):
        for i in range(50):
            self.face = random.randint(0, 1)
            if self.face == 1:
                self.cnt_front += 1
            else:
                self.cnt_back += 1
        return self.cnt_front, self.cnt_back
## 메인 코드 부분 ##
coin_count=[]
coin_list=[]
coin_cnt=int(input("코인 개수 :"))
for i in range(coin_cnt):
    coin_list.append(i)
    coin_list[i]=Coin()
    coin_count = coin_list[i].face_count()
    print("%d번 동전을 50번 던진 결과 앞면은 %d번, 뒷면은 %d번 나옴" % (i+1, coin_count[0], coin_count[1]))
# myCoin1과 myCoin2 50번씩 던져서 앞면과 뒷면 개수 세기
# 동전 던진 결과 출력