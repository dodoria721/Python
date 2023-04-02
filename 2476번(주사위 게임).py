N = int(input())

result = []
for _ in range(N):
    a, b, c = map(int, input().split())

    if a == b == c:
        result.append(10000+a*1000)
    elif a == b or a == c:
        result.append(1000+a*100)
    elif b == c:
        result.append(1000+b*100)
    else:
        dice = [a, b, c]
        result.append(max(dice) * 100)

print(max(result))