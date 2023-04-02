case = int(input())
score = 0

for _ in range(case):
    data = input()

    if data == '1':
        score += 1

if score > (case - score):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")