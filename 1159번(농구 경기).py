N = int(input())
player = {}

for _ in range(N):
    name = input().strip()
    if name[0] in player: #첫 글짜가 있을때
        player[name[0]] += 1
    else:                 #첫 글짜가 없을때
        player[name[0]] = 1

player = dict(sorted(player.items())) # 사전순 대로 정렬

result = ''
for key, value in player.items():
    if value >= 5:
        result += key

if result:
    print(result)
else:
    print('PREDAJA')