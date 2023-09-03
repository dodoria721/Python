n = int(input()) # 테스트 케이스

for x in range(n):
    p = int(input()) # 고려해야될 선수의 수
    max_price = 0

    for y in range(p):
        price, player = input().split()

        if max_price < int(price):
            max_price, max_player = int(price), player
            
    print(max_player)