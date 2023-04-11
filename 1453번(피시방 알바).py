N = int(input())

seat = list(input().split())
count = 0

lst = []
for x in seat:
    if x in lst:
        count += 1
    else:
          lst.append(x)

print(count)