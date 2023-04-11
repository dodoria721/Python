a, b = input().split()

sum_b = 0
for x in b:
     sum_b += int(x)

result = 0
for y in a:
     result += int(y) * sum_b

print(result)