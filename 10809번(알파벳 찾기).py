S = input()
alphabet = {chr(i): -1 for i in range(ord('a'), ord('z')+1)}

for x in range(len(S)):
    if S[x] in alphabet and alphabet[S[x]] == -1:
        alphabet[S[x]] = x

for y in alphabet.values():
    print(y, end= ' ')