import random

#create a list of students using input
students = []
number = int(input('The number of students is: '))
for _ in range(number):
    student = input('Student name: ')
    students.append(student)
    
#create a list of numbers of questions
questions = []
number = int(input('Number of questions is: '))
for _ in range(1, number + 1):
    questions.append(_)
    
#create a dictionary 'name': 'question number'
exam = {}
for student in students:
    exam[student] = random.choice(questions)
    questions.remove(exam[student])
    print(student.title() + ' has question number ' + str(exam[student]))
