import sys

fbi = []
for x in range(5):
     name = sys.stdin.readline().strip()

     if 'FBI' in name:
          fbi.append(x)
     
if fbi:
     for x in fbi:
          print(x+1,end=' ')
else:
     print('HE GOT AWAY!')