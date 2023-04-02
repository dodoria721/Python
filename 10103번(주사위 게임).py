n = int(input())

chan, sang = 100, 100
for _ in range(n):
    c, s = map(int, input().split())

    if c == s:
        continue
    elif s < c:
        sang -= c
    elif c < s:
        chan -= s

print(chan)
print(sang)