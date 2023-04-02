T = int(input())

for _ in range(T):
    Yonsei = 0
    Korea = 0
    for _ in range(9):
        Yscore, Kscore = map(int, input().split())
        Yonsei += Yscore
        Korea += Kscore

    if Yonsei > Korea:
        print("Yonsei")
    elif Yonsei < Korea:
        print("Korea")
    elif Yonsei == Korea:
        print("Draw")