#배(0) 등(1)

for _ in range(3):
    status = list(input().split())

    count_0 = status.count('0')
    count_1 = status.count('1')

    if count_0 == 1 and count_1 == 3: #도
        print('A')
    elif count_0 == 2 and count_1 == 2: #개
        print('B')
    elif count_0 == 3 and count_1 == 1: #걸
        print('C')
    elif count_0 == 4: #윷
        print('D')
    elif count_1 == 4: #모
        print('E')