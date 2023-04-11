while True:
     length = 0
     N = input()
     if N == '0':
          break
    
     for x in N:
          if x == '1':
               length += 2
          elif x == '0':
               length += 4
          else:
               length += 3

     length = length + (len(N)+1) 
     print(length)
