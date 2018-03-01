# Problem: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':

    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    unique_student_score = list(set([student_score[1] for student_score in students]))
    unique_student_score.sort()

    second_grade = unique_student_score[1]
    second_grade_student = []
    for student_score in students:
        if student_score[1] == second_grade:
            second_grade_student.append(student_score[0])

    second_grade_student.sort()
    [print(name) for name in second_grade_student]
