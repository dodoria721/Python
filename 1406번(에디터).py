'''L: 커서를 왼쪽으로 한 칸 옮김
   D: 커서를 오른쪽으로 한 칸 옮김
   B: 커서 왼쪽에 있는 문자를 삭제함
   P $: $라는 문자를 커서 왼쪽에 추가함'''

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])
st1.extend(reversed(st2))
print(''.join(st1))