N, M = map(int, input().split()) #가로, 세로

row_count = 0
col_count = 0

status = []
for _ in range(N):
    status.append(input())

for i in status:
    if 'X' not in i:
        row_count += 1

for j in range(M):
     found_x = False
     for k in range(N):
          if status[k][j] == 'X':
               found_x = True
               break
     if not found_x:
          col_count += 1
     

print(max(row_count, col_count))