def convert_grade_to_word(grade):
    if 2.00 <= grade <= 2.99:
        return 'Fail'
    if 3.00 <= grade <= 3.49:
        return 'Poor'
    if 3.50 <= grade <= 4.49:
        return 'Good'
    if 4.50 <= grade <= 5.49:
        return 'Very Good'
    if 5.50 <= grade <= 6.00:
        return 'Excellent'


student_grade = float(input())
result = convert_grade_to_word(student_grade)
print(result)
