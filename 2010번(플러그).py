import sys
input = sys.stdin.readline

N = int(input().strip())

sum = 0
for _ in range(N):
    sum += int(input().strip())

print(sum-(N-1))