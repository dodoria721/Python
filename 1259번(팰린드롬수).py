while(True):
    data = input()
    if data == '0':
        break

    left_side = [x for x in data]
    right_side = [x for x in data[::-1]]

    status = True
    for index in range(len(data)):
        if left_side[index] != right_side[index]:
            status = False

    if status:
        print("yes")
    else:
        print('no')