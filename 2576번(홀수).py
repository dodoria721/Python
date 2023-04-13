odd_lst = []

for _ in range(7):
    n = int(input())

    if n % 2 != 0:
        odd_lst.append(n)

if odd_lst:
    print(sum(odd_lst))
    print(min(odd_lst))
else:
    print(-1)