#202003302권준오

#
# 5. MM/DD/YY 형태의 날짜를 입력받아 YY/MM/DD 로 출력
#
'''
date1 = input("날짜 입력(MM/DD/YY) : ")
date1_list = date1.split('/')
date_result = date1_list.pop()
date1_list.insert(0,date_result)
print(date1_list)
date2 = '/'.join(date1_list)
print("변환날짜(YY/MM/DD) : ",end='')
print(date2)
'''
#
# 6. 단어(문자, 숫자)가 공백으로 구분되는 문장에서 숫자 추출. 
#
sentence = "2022 python 2 programming"
print(sentence)
list_sentence=sentence.split(" ")
list_digit=[]
print(list_sentence)
for i in list_sentence:
    if i.isdigit()==True:
        list_digit.append(i)
print("숫자 추출 결과(리스트) :",list_digit)
#
#
#
