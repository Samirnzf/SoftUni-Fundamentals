from math import ceil
people_in_elevator = int(input())
capacity_of_elevator = int(input())
courses = ceil(people_in_elevator / capacity_of_elevator)

print(courses)
