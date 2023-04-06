while 1:
    n = int(input())

    if n == -1:
        break

    data = []
    result = 0
    for x in range(1, n):
        if n % x == 0:
            data.append(x)
            result += x

    if n == result:
        b = ' + '.join(map(str,data))
        print(n,'=',b)
    else:
        print(f'{n} is NOT perfect.')