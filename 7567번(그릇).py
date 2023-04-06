data = list(input())
result = 10

for x in range(len(data)-1):
    if data[x] != data[x+1]:
        result += 10
    else:
        result += 5

print(result)