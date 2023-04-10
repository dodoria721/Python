lst = []

for _ in range(5):
    a = list(map(int, input().split()))
    lst.append(sum(a))

print('{0} {1}'.format(lst.index(max(lst))+1, max(lst)))