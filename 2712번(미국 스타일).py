case = int(input())

for _ in range(case):
    data = input().split()

    if '.' in data[0]:
        data[0] = float(data[0])
    else:
        data[0] = int(data[0])

    if data[1] == 'kg':
        num = data[0] * 2.2046
        print(f'{num:.4f} lb')
    elif data[1] == 'lb':
        num = data[0] * 0.4536
        print(f'{num:.4f} kg')
    elif data[1] == 'l':
        num = data[0] * 0.2642
        print(f'{num:.4f} g')
    elif data[1] == 'g':
        num = data[0] * 3.7854
        print(f'{num:.4f} l')