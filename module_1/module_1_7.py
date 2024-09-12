# student: Andrey Jaroslavtsev


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
grades_average = list(map(lambda *args: sum(*args)/len(*args),grades))
dict_ = dict(zip(students_list,grades_average))
print(dict_)