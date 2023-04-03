chesse_list = []
for _ in range(8):
    chesse = list(input())
    chesse_list.append(chesse)

count = 0
for x in range(8):
    if (x % 2 == 0): # 짝수 줄
        for y in range(0,8,2):
            if chesse_list[x][y] == 'F':
                count += 1

    else: #홀수 줄
        for j in range(1,8,2):
            if chesse_list[x][j] == 'F':
                count += 1

print(count)