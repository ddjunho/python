#202003302권준오

#
#8. get()함수 예제
#
'''
dictionary = { "name": "건조 망고", "type": "당절임", "origin": "필리핀" }
print("값 :",dictionary["name"])
value2 = dictionary.get("year")
print("값 :",value2)
if (value2 == None) :
    print("존재하지 않는 키에 접근했었음.")
   ''' 
#
#9. in 키워드 예제
#
dictionary = { "name": "건조 망고", "type": "당절임", "origin": "필리핀" }
key = input("> 접근하고자 하는 키 :")
access = key in dictionary
if  access == False:
    print("존재하지 않는 키에 접근")
elif access== True:
    print(dictionary[key])


#
#
#
