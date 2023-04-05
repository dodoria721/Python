import sys
sys.setrecursionlimit(10**9)
num_list = []

while True:
    try:
        num = int(input())
        num_list.append(num) # 1.num_list = [50,30,24,5,28,45,98,52,60]
    except:
        break

def postorder(first,end): # 3. first = 0, end = 8
    if first > end: # 0 > 8 False
        return
    mid = end+1 # mid = 9
    for i in range(first+1, end+1): # range(1,9) 1,2,3,4,5,6,7,8
        if num_list[first] < num_list[i]: # num_list[0] = 50, num_list[1] = 30 Flase
            mid = i
            break
    
    postorder(first+1, mid-1) #postorder(1, 8)
    postorder(mid, end)
    print(num_list[first])

postorder(0, len(num_list)-1) # 2.postorder(0, 8) //len(num_list) = 9