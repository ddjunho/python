#202003302권준오

#
#10. 딕셔너리를 이용하여 친구들 이름과 핸드폰 번호 저장
#
'''
contacts= {}
while True:
    key = input("이름:")
    if key == "":break
    value = input("번호:")
    contacts[key] = value
print("연락처",contacts)
friend = input("친구이름?")
print(contacts[friend])
'''
#
#11. 딕셔너리를 이용하여 편의점 재고 관리 프로그램
#
items = {"커피":7, "생수":3, "종이컵":10, "우유":5, "콜라":4, "사이다":11}
print(items)
while True:
    sell = input("판매한 물건은? ")
    if items.get(sell) == None:
        print("그런거 없음")
        print(items)
        break
    items[sell] -= 1
    
    if items[sell] < 1:
        print("재고 다떨어짐 ")
        break
    print(items)
#
#
#
