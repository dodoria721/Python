N, M = map(int, input().split())

lst1 = []
lst2 = []

for _ in range(N):
    data = list(map(int, input().split()))
    lst1.append(data)
    
for _ in range(N):
    data = list(map(int, input().split()))
    lst2.append(data)

for x in range(N):
    for y in range(M):
        print(lst1[x][y] + lst2[x][y],end=' ')
    print('')