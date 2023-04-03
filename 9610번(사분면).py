n = int(input())

quadrant = {'Q1' : 0, 'Q2' : 0, 'Q3' : 0, 'Q4':0, 'AXIS' : 0}
for _ in range(n):
    a, b = map(int,input().split())

    if (a > 0) and (b > 0):
        quadrant['Q1'] += 1
    elif (a < 0) and (b > 0):
        quadrant['Q2'] += 1
    elif (a < 0) and (b < 0):
        quadrant['Q3'] += 1
    elif (a > 0) and (b < 0):
        quadrant['Q4'] += 1
    else:
        quadrant['AXIS'] += 1

for key, value in quadrant.items():
    print(f'{key}: {value}')
