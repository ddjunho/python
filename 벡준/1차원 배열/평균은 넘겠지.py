c = int(input())
for i in range(c):
    n = list(map(int, input().split()))
    count = 0
    for j in n[1:]:
        if j> sum(n[1:])/len(n[1:]):
            count +=1
    print("%.3f" %(count/n[0] *100) + "%")
