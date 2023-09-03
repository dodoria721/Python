n = int(input())  # 사람 수
people = []

for _ in range(n):
    name, day, month, year = input().split()
    birth_date = (int(year), int(month), int(day))
    people.append((name, birth_date))


oldest_person = None
youngest_person = None
oldest_date = None
youngest_date = None

for person in people:
    name, date = person
    if oldest_date is None or date < oldest_date:
        oldest_date = date
        oldest_person = name
    if youngest_date is None or date > youngest_date:
        youngest_date = date
        youngest_person = name

print(youngest_person)
print(oldest_person)
