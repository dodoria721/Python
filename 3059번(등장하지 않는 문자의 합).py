case = int(input())

for _ in range(case):
    s = set(input())
    ord_sum = 0

    for x in s:
        ord_sum += ord(x)

    print(2015 - ord_sum) # A~Z 아스키코드 합 2015