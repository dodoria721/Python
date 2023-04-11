data = input().upper()

word = {}
for x in data:
     if x in word:
          word[x] += 1
     else:
          word[x] = 1

max_count = max(word.values())
max_word = [k for k, v in word.items() if v == max_count]

if len(max_word) == 1:
     print(max_word[0])
else:
     print('?')