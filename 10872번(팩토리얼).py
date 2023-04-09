def fectorial(n):
    if n == 0:
        return 1
    else:
        return n * fectorial(n-1)
    
print(fectorial(int(input())))