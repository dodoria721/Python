import sys

for _ in range(3):
    num = []
    case = int(sys.stdin.readline().strip())

    for _ in range(case):
        num.append(int(sys.stdin.readline().strip()))

    S = sum(num)

    if S == 0:
        print(0)
    elif S > 0:
        print('+')
    else:
        print('-')