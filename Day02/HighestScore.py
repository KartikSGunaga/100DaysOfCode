student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest = student_scores[0]

for i in range(1, len(student_scores)):
    if(student_scores[i] > highest):
        highest = student_scores[i]

print(highest)

