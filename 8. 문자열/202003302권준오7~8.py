#202003302권준오

#
# 7. 주어진 문장에서 가장 긴 단어를 출력하는 프로그램
#
'''
sentence = "오래 보아야 사랑스럽다 너도 그렇다. 나태주"
list_word = sentence.split(" ")
print(sentence)
longest = 0
for i in list_word:
    if len(i)>longest:
        longest=len(i)
        longest_word = i
print("가장 긴 단어:",longest_word)
'''
#
# 8. 주어진 문장에서 문자의 빈도를 계산하여 딕셔너리에 저장
#
sentence = 'Hello Hey'
dict = {}
for key in list(sentence):
    if key in dict:
        dict[key] +=1
    else:
        dict[key] = 1
print("문장 :",sentence)
print("결과(딕셔너리) :",dict)
