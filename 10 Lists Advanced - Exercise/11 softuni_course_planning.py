lessons_and_exercises = input().split(', ')
course_plan_list = []
while True:
    command = input().split(":")
    if command[0] == "course start":
        break

    operation, lesson_title, index = command

    if operation == 'Add':
        course_plan_list.append(lesson_title)
    elif operation == 'Insert':
        course_plan_list.insert(int(index), lesson_title)
    elif operation == 'Remove':
        if lesson_title in course_plan_list:
            course_plan_list.remove(lesson_title)
    elif operation == 'Swap':
        if lesson_title in course_plan_list:
            course_plan_list[index], course_plan_list[lesson_title] = course_plan_list[lesson_title], course_plan_list[index]


