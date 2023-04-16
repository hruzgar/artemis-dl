import utils

course_name = 'Praktikum: Grundlagen der Programmierung WS22/23'
exercise_name = 'W02P02 - Kontrollstrukturen I'

print(course_name)
print(exercise_name)
print('***')
print(utils.get_valid_filename(course_name))
print(utils.get_valid_filename(exercise_name))
print('***')
print(utils.slugify(course_name))
print(utils.slugify(exercise_name))