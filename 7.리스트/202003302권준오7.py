#202003302권준오

#
#7. 딕셔너리 생성, 길이, 추가, 수정, 삭제
#
cafe = {"아메리카노":2000, "카푸치노": 3000}
print(cafe)
print(len(cafe))
cafe["스무디"]= 3500
print(cafe)
cafe["아메리카노"]= 2500
print(cafe)
del cafe["카푸치노"]
print(cafe)
for i in cafe:
    print(i, end='->')
    print(cafe[i])
#
#
#

#
#
#
