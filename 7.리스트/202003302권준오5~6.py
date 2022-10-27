'''
#202003302권준오

#
#5. 5개의 숫자 입력받아 평균구하기
#
a = list(map(int,input("숫자 입력 한칸씩 띄어서 5개 : ").split()))
hap = sum(a)
avg = hap/len(a)

print("평균 ==> %3.1f" % avg)
#
#6. 5개의 숫자를 입력받아 최소, 최대값 구하기
#
'''
a = [0, 0, 0, 0, 0]
for i in range(0,5) :
    a[i] = int(input(str(i+1) + "번째 숫자 : " ))   



print("최소 %d, 최대 %d " % (min(a), max(a)))

