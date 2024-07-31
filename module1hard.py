grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_Sum = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]),
            sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]),
            sum(grades[4]) / len(grades[4])]

students = list(students)
students.sort()
grades = grades_Sum


a = { students[0]: grades[0], students[1]: grades[1], students[2]: grades[2],
      students[3]: grades[3], students[4]: grades[4],}

print(a)
print(type(a))