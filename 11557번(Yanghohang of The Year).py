T = int(input()) # case 숫자

for _ in range(T):
    N = int(input()) # 학교의 숫자
    school = {}
    for _ in range(N):
        name, number = input().split()
        school[name] = int(number)
    print('{}'.format(max(school, key=school.get)))