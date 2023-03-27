student = [0] * 5
sum = 0

for x in range(5):
    grade = int(input())

    if(grade < 40):
        student[x] = 40
    else:
        student[x] = grade

    sum += student[x]

    
print(int(sum/5))