'''
## code11-01 : 파일에서 데이터 읽어 화면에 출력

inFp = None    # 입력 파일
inStr = ""        # 읽어온 문자열

# C:\\python\\data1.txt 파일을 읽기 모드로 열기

inFp =

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

# 파일 닫기


'''
'''
## code11-02: 텍스트 파일에 있는 모든 행을 한행씩 읽고 출력

inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열

inFp = open("C:\\python\\data1.txt", "r")

while True :
    inStr = ________________  # 한 줄씩 읽기
    if inStr == "" :
        break;
    _________________________  # 출력하기

_________________  # 파일 닫기
'''
'''
## code11-03: 파일 내용을 한꺼번에 읽어 출력
## readlines()함수 : 파일의 내용을 통째로 읽어서 리스트에 저장 

inFp = None
inList = ""

inFp = open("C:\\python\\data1.txt", "r")

# 파일 한꺼번에 읽기
 

print(inList)

inFp.close()
'''
'''
## code11-03-1 : close() 호출하지 않고 프로그램 종료하는 방법

inFp = None
inList = ""

# close() 호출하지 않고 프로그램 종료
______ open("C:\\python\\data1.txt", "r") ____ inFp:
    inList = inFp.readlines()
    print(inList)
'''
'''
## code11-04 : readlines()함수를 사용하지만 한 행씩 출력

inFp = None
inList, inStr = [], ""

inFp = open("C:\\python\\data1.txt", "r")

inList = inFp.readlines()

# 한 행씩 출력



inFp.close()

'''
'''
## code11-05 : 파일명 입력받아 파일 내용 출력

inFp = None
fName, inList, inStr = "", [ ], ""

fName = ___________________  # 파일명 입력받기
inFp = open(fName, "r")

inList = _________________ # 파일 내용을 한꺼번에 읽기
for inStr in inList :
    print(inStr, end = "")

inFp.close()
'''
'''
## code11-06: 파일명 입력받아 파일 내용 출력 2
## 파일 없을 때 오류 처리 :  os.path.exists(파일명) 

_____________  # 파일 없을때 오류 처리 위한 import

inFp = None
fName, inList, inStr = "", [], ""

fName = input("파일명 : ")

___________________________  # 파일이 있다면
    inFp = open(fName, "r")

    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end="")

    inFp.close()
else:
    print("%s 파일이 없습니다" % fName)
'''
'''
## code11-07 : 키보드로 입력한 내용을 한 행씩 파일에 쓰기

outFp = None
outStr = ""

# C:/python/data3.txt 을 쓰기모드로 열기
outFp = ________________________________

while True:
    outStr = input("내용 입력 : ")
    if outStr != "" :
        ____________________________ # 파일에 내용 쓰고 \n 추가하기
    else :
        break

outFp.close()
print("--- 파일에 정상적으로 써졌음 ---")
'''
'''
## code11-08 : 파일 복사


inFp, outFp = None, None
inStr = ""

# c:\\python\\data3.txt 파일은 읽기 모드로, c:\\python\\data5.txt는 쓰기 모드로 열기

inFp = ____________________________________
outFp = ____________________________________

inList = _________________ # 파일을 한꺼번에 읽기
for inStr in inList :
    ________________________ # 파일에 한줄씩 쓰기

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")
'''

'''
## code11-09: 기존 파일에 내용 추가하기

# c:\\python\\data1.txt 파일을 추가 모드로 열기
f = ____________________________

for i in range(1, 6):
    data = "%d번째 줄.\n" % i
    f.write(data)
    
f.close()
'''

'''
## code11-10: 이진 파일(예: notepad.exe)의 복사

inFp, outFp = None, None
inStr = ""

# C:/windows/notepad.exe 파일을 바이너리 읽기모드로 열고. C:/python/notepad.exe을 바이너리 쓰기 모드로 열기

inFp = ________________________________

outFp = ________________________________

while True :
    inStr = ___________ # 바이너리 파일 읽기
    if not inStr :
        break
    ____________________ # 바이너리 파일 쓰기

inFp.close()
outFp.close()
print("--- 이진 파일이 정상적으로 복사되었음 ---")
'''