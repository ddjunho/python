'''
#202003302권준오

#
#7-1. 리스트 초기화, 요소 값 수정
#
list_a = [100, 20.5, "파이썬", "가을", "True"]

del(list_a[0])
list_a.insert(0,2022)
print(list_a)

#
#7-2. 리스트 연산(연결, 반복, 길이)
#
'''
a = [10, 20]
b = [30, 40, 50]
a.extend(b)
c =a
a.extend(a)
d= a
e = len(a)


print("리스트 a와 b 연결 : ", c)
print("리스트 a를 두번 반복 : ", d)
print("리스트 a 길이 : ", e)
