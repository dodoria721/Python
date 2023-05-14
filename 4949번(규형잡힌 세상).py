import sys
input = sys.stdin.readline

while True:
    data = input().rstrip()
    bracket = []
    if data[0] == '.':
        break

    matching = {')': '(', ']': '['}  # 괄호 매칭 딕셔너리

    for x in data:
        if x == '(' or x == '[':  # 열린 괄호면 리스트에 추가
            bracket.append(x)
        elif x == ')' or x == ']':  # 닫힌 괄호면 매칭 검사
            if bracket and bracket[-1] == matching[x]:  # 매칭되는 열린 괄호가 있으면 제거
                bracket.pop()
            else:
                bracket.append(x) 

    if bracket:  # 괄호의 균형이 맞지 않으면 no 출력
        print('no')
    else:
        print('yes')  # 괄호의 균형이 맞으면 yes 출력
