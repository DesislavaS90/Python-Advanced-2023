number_of_students = int(input())

student_data = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in student_data:
        student_data[student] = []
    student_data[student] += [float(grade)]

for s, g in student_data.items():
    grade = ' '.join(map(lambda grade: f'{grade:.2f}', g))
    average = sum(g) / len(g)
    print(f'{s} -> {grade} (avg: {average:.2f})')