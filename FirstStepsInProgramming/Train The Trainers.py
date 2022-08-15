jury_numbers = int(input())
sum_grades = 0
total_grades = 0
presentation_counter: int = 0
name_presentation = input()
while True:
    presentation_counter += 1
    for i in range(jury_numbers):
        grade = float(input())
        sum_grades += grade
        average_grade_per_presentation = sum_grades / jury_numbers
    print(f'{name_presentation} -{average_grade_per_presentation: .2f}.')
    total_grades += average_grade_per_presentation
    sum_grades = 0

    name_presentation = input()
    if name_presentation == 'Finish':
        break
total_grades_print = total_grades / presentation_counter
print(f"Student's final assessment is{total_grades_print: .2f}.")