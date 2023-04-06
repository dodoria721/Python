case = int(input())

for _ in range(case):
    data = input().split('X') # X를 기준으로 쪼개기
    data = [x for x in data if x != '']# '' 삭제

    result = 0
    for i in data:
        n = len(i)
        result += n*(1+n)/2 # 등차수열 합

    print(int(result))