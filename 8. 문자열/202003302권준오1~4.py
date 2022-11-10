#202003302권준오
'''
#
# 1. 사용자가 입력한 단어의 끝에 'ing' 추가하는 프로그램
#
mystr = input("입력단어 :")
print("출력단어 :", mystr, end ="ing")

#
# 2. 사용자가 입력한 단어의 길이가 2보다 크면 문자열 끝에 'ing' 추가하고
# 그렇지 않으면 입력한 단어를 그대로 출력하는 프로그램
mystr = input("입력 단어: ")
if len(mystr) >2:
    print("출력단어 :", mystr, end ="ing")
else:
    print("출력단어 :", mystr)

#
# 3. 사용자가 입력한 단어의 끝에 'ing' 추가하는 프로그램
# 단, 입력한 단어가 'ing'으로 끝나면 'ly' 추가
mystr = input("입력 단어: ")

if mystr.endswith("ing") == True:
    print("출력단어 :", mystr, end ="ly")
else:
    print("출력단어 :", mystr, end ="ing")
'''
#
# 4. 주어진 문장에서 '가을'을 찾아 'autumn'으로 변경
#
mystr = '봄 여름 가을 겨울'

print("문장 :",mystr)
print("변경문장 :",mystr.replace("가을","autumn"))
