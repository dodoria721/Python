total = 0 # 총 사람수
max = 0 # 최대 사람 수

for _ in range(4):
    a,b = map(int, input().split()) # 내린 사람, 탄 사람
    
    total = total + b - a

    if total >= max:
        max = total

print(max)