x1, y1 = map(int, input().split()) #첫 번째 점
x2, y2 = map(int, input().split()) #두 번째 점
x3, y3 = map(int, input().split()) #세 번째 점

if x1 == x2: A = x3
elif x1 == x3: A = x2
else: A = x1

if y1 == y2: B = y3
elif y1 == y3: B = y2
else: B = y1

print(A, B)