while 1:
    a = input()
    if a == "# 0 0":
        break
    else:
        a = a.split()

        if int(a[1]) > 17 or int(a[2]) >= 80:
            print(a[0], "Senior")
        else:
            print(a[0], "Junior")