# list methods by using append
courses = ['history', 'physics', 'maths', 'science']

courses.append('arts')
print(courses)

# list methods by using insert
courses = ['history', 'physics', 'maths', 'science']

courses.insert(0, 'arts')
print(courses)

# list methods by using extend method
courses = ['history', 'physics', 'maths', 'science']
courses_2 = ['arts', 'education']

courses.insert(0, courses_2)
print(courses)

# One more example of insert method
courses = ['history', 'physics', 'maths', 'science']
courses_2 = ['arts', 'education']

courses.insert(0, courses_2)
print(courses[0])

# one more example of extend method
courses = ['history', 'physics', 'maths', 'science']
courses_2 = ['arts', 'education']

courses.extend(courses_2)
print(courses)

# How we want to remove some items form the list
courses = ['history', 'physics', 'maths', 'science']
courses.remove('maths')
print(courses)

# Use pop method to remove the items form list
courses = ['history', 'physics', 'maths', 'science']
courses.pop()
print(courses)

# Sort method
courses = ['history', 'physics', 'maths', 'science']
courses.sort()
print(courses)

# Sort method by using numbers
numbers = [1, 7, 3, 5, 2]
numbers.sort()
print(sum(numbers))

# sorted method
courses = ['history', 'physics', 'maths', 'science']
sorted_courses = sorted(courses)

print(sorted_courses)

# check true or false 
courses = ['history', 'physics', 'maths', 'science']
print('maths' in courses)

# for loop
courses = ['history', 'physics', 'maths', 'science']
for course in courses:
    print(course)

# for loop one more example
courses = ['history', 'physics', 'maths', 'science']
for index, course in enumerate(courses, start=1):
    print(index, course)

# join method
courses = ['history', 'physics', 'maths', 'science']
course_str = '- '.join(courses)
print(course_str)