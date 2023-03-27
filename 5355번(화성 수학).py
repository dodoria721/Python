T = int(input())

for x in range(T):
     data = input().split()
     
     a = float(data[0])
     for y in range(len(data)):

        if data[y] == '@':
            a *= 3
        elif data[y] == '%':
            a += 5
        elif data[y] == '#':
            a -= 7
        
     print("{:0.2f}".format(a))