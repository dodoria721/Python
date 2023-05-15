from collections import deque

N = int(input())
cards = deque(range(1, N+1))
print(cards)

while len(cards) > 1:
    cards.popleft()
    print("첫장 버리기", cards)
    cards.rotate(-1)
    print("첫장 마지막에 넣기", cards)

print(cards[0])