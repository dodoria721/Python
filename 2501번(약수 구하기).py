# N의 약수들 중 K번째로 작은 수를 출력하는 프로그램
N, K = map(int, input().split())
num = []

for x in range(1, N+1):
    if N % x == 0: # 약수일때
        num.append(x)

num = list(sorted(num))

if len(num) < K:
    print(0)
else:
    print(num[K-1])