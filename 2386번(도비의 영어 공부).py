while True:
    data = input().lower()
    if data == '#':
        break

    print(data[0], data[2:].count(data[0]))