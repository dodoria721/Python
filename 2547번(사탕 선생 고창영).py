import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스

for _ in range(T):
    temp = input() # 빈 줄로 구분
    N = int(input()) # 학생 수
    total = 0 # 총 사탕 수

    for _ in range(N):
        candy = int(input())
        total += candy

    if total % N == 0: # 사탕을 나눠줄 수 있는 경우
        print('YES')
    else:
        print('NO')