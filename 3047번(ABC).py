#A < B < C

num_3 = list(map(int, input().split()))
data = input()

dic = {'A': 0, 'B': 0, 'C': 0}

max = max(num_3)
dic['C'] = max
num_3.remove(max)

min = min(num_3)
dic['A'] = min
num_3.remove(min)

dic['B'] = num_3[0]

for x in data:
    print(dic[x], end=' ')