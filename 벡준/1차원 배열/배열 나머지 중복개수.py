n = []
for i in range(10):
    i=int(input())
    n.append(i%42)
n=list(set(n))#중복된 자료형 제거 (set)
print(len(n))