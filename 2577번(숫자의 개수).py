A = int(input())
B = int(input())
C = int(input())
lst = list(str(A*B*C))

dic = {'0': 0, '1': 0, '2':0, '3':0, '4':0, '5':0, '6':0,'7':0,'8':0,'9':0}

for x in lst:
    dic[x] += 1

for y in dic.values():
    print(y)