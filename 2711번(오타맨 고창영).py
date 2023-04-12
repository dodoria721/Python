case = int(input())

for _ in range(case):
    data = input().split()
    lst = data[1]

    idx = int(data[0])
    lst = lst[:idx-1] + lst[idx:]

    print(lst)