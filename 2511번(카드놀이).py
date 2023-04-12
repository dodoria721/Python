A = input().split()
B = input().split()

A_score = 0
B_score = 0

for x in range(10):
    if A[x] == B[x]:
        A_score += 1
        B_score += 1
    elif A[x] > B[x]:
        A_score += 3
    else:
        B_score += 3

print(A_score, B_score)

if A_score > B_score:
    print('A')
elif B_score > A_score:
    print('B')
else: # 점수가 같은 경우
    count = 0
    for x in range(9,-1,-1):
        count += 1
        if A[x] != B[x]:
            break
    if A[x] > B[x]:
        print('A')
    elif A[x] < B[x]:
        print('B')

    if count == 10: #숫자 다 똑같은 경우
        print('D')