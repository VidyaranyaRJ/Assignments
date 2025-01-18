# Question 3: Calculate grade based on percentage
marks = []
for subject in ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'Computer']:
    marks.append(float(input(f"Enter marks for {subject}: ")))

percentage = sum(marks) / 5
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

print(f"Percentage: {percentage}%\nGrade: {grade}")
