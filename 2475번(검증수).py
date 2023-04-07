a = list(map(int, input().split()))

sum = 0
for x in range(5):
    sum += a[x]**2

print(sum%10)