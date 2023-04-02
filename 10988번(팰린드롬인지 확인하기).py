word = list(input())
length = len(word)
count = 0

for x in range(int(length/2)):
    if word[x] == word[length - (x+1)]:
        count += 1

if count == (int(length/2)):
    print(1)
else:
    print(0)