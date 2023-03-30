# ================ 첫번째 코드 ==================
t, m, s = map(int, input().split()) #시간, 분, 초
cook = int(input()) #요리하는데 필요한 시간 초

m += cook//60 #요리 후 바뀐 분
s += cook%60 #요리 후 바뀐 초

if s == 60:
    m+=1
    s=0
elif s > 60:
    m = m + (s//60)
    s = s%60

if m == 60:
    t += 1
    m = 0
elif m > 60: 
    t = t + (m//60)
    m = m%60

if t >= 24:
    t %= 24

print(t, m, s)

#================= 두번째 코드 ============

a, b, c = map(int, input().split())
cook = int(input())

total_second = (a * 3600) + (b*60) + c + cook

t = total_second // 60 //60 % 24
m = total_second // 60 % 60
s = total_second % 60

print(t,m,s, sep=' ')

#=============== 새번째 코드 =============

a, b, c = map(int, input().split()) #시간, 분, 초
cook = int(input()) #요리하는데 필요한 시간 초 ex) 200

total_second = (a * 3600) + (b*60) + c + cook

t = total_second // 3600 % 24 # second to time
m = (total_second % 3600) // 60 % 60 # time to minute
s = total_second % 60 % 60 # remaining seconds

print(t,m,s, sep=' ')