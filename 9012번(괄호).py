import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    PS = input().strip()
    tmp = []
    for x in PS:
        if x == '(':
            tmp.append(x)
        else:
            if '(' in tmp:
                tmp.remove('(')
            else:
                tmp.append(x)

    if tmp:
        print('NO')
    else:
        print('YES')