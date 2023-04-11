N = int(input())
score = input().split('0')
score = [x.strip() for x in score if x.strip()]

result = 0

for x in score:
     if len(x) == '1':
          result += 1
     else:
          count = x.count('1')
          result += count * (1 + (count*1))//2

print(result)