T = int(input())

for i in range(T): # T = 2
    R, S = input().split() # 3 ABC
    input_x = list(S) # input = ['A', 'B', 'C']
    P = ''

    for j in range(len(input_x)): # len(input) = 3
        input_x[j] = input_x[j] * int(R)
        P += input_x[j]

    print(P)