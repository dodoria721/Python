L = int(input()) # 방학
A = int(input()) # 수학
B = int(input()) # 국어
C = int(input()) # 하루 수학
D = int(input()) # 하루 국어

if A % C == 0:
    data1 = A//C 
else:
    data1 = (A//C)+1

if B % D == 0:
    data2 = B//D
else:
    data2 = (B//D)+1

print(L-max(data1,data2))