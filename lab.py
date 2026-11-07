students = [
    {"name" : "Tom", "grade" : 5},
    {"name" : "Bob",  "grade" : 4},
    {"name" : "Sam", "grade" : 4},
    {"name" : "George", "grade" : 3},
    {"name" : "Alice", "grade" : 4},
    {"name" : "Bob",  "grade" : 5},
    {"name" : "Tom", "grade" : 3},
]

print("Исходный список студентов")
for item in students:
    print(item)

first = students[0]
print("\nПервый студент полученный по индексу 0:")
print(first)

first_three = students[:3]
print("\nСрез: первые три")
for item in first_three:
    print(item)

new = {"name": "Frodo","grade": 4}
students.append(new)
print("\nСписок после добавления нового студента")
for item in students:
    print(item)

students[3] ["grade"] = 4
print("\nЭлемент после изменения")
print(students[3]) 

removed = students.pop()
print("\nУдаленный студент")
print(removed)

print("\nСписок после удаления последнего студента")
for item in students:
    print(item)

names = set()
for item in students:
    names.add(item["name"])
print("\nМножество студентов")
print(names)

has_Alice = "Alice" in names
print("\nЕсть ли студент Alice:", has_Alice)

best_grades = [item for item in students if item["grade"]==5]
print("\nОценки 5")
for item in best_grades:
    print(item)

sorted_grades = sorted(students, key=lambda item: item["grade"])
print("\nОтсортированный список по возрастанию")
for item in sorted_grades:
    print(item)

sorted_grades = sorted(students, key=lambda item: item["grade"], reverse=True)
print("\nОтсортированный список по убыванию")
for item in sorted_grades:
    print(item)

sum_grade = 0
for item in students:
    grade = item["grade"]
    sum_grade += grade
average_grade = sum_grade / len(students)
print("\nСредний балл студентов", average_grade)

formatted = [
    f"{item['name']} - {item['grade']}"
    for item in students
]
print("\nВыводим преобразованный список студентов")
for item in formatted:
    print(item)

student_info = {"firstname" : "Frodo", "lastname" : "Beggins"}
print("\nСловарь информации о студенте")
print(student_info)

firstname = student_info["firstname"]
print("\nВывод имени по ключу")
print(firstname)

student_info["lastname"] = "Sauron"
print("\nСловарь после изменения")
print(student_info)

print("\nКлючи словаря")
for key in student_info.keys():
    print(key)

print("\nЗначения словаря")
for value in student_info.values():
    print(value)