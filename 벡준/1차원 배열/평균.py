n=int(input())
num = list(int(input().split()))
m = max(num)


for i in n:
    num.append(score/max_score *100)
print(sum(num)/m)
