# 1. Created the `hello-world.py` file to print to the hello world #

check `01-hello-world.py`

# 2. Strings #

## single quote vs double quote difference ##

`Input:` 'Viswa's World'
`Output:` invalid syntax error it will consider as a multiple strings

`Fix:` 'Viswa\'s World' we have added escape `\` character to fix the syntax and the better way to do is add the double quotes "Viswa's World" so that it will consider as a single string.

while using the single quote  it will through a error called invalid syntax, since it will consider as a multiple strings.
We need to avoid that we have a solution or use the double quotes "Bobby's World"

## multiple line string using triple double quotes ##

Once we execute the triple double qoutes it will print in multiple lines

`Input:`

```bash
"""Viswa's World was fantastic 
in the 1990's"""
```
`Output:` Viswa's World was fantastic 
          in the 1990's
## Length Function ##
message = "Hello World"
print(len(message))

## Index characters in string using square brackets [] ##
message = "Hello World"
print(message[10])

`Output:` d
## Range of Characters ##
message = "Hello World"
print(message[0:5])

`Output:` Hello

Difference b/w methods and function, same thing for now.

## String methods lower() & upper()  ##
message = "Hello World"
print(message.upper())

message = "Hello World"
print(message.lower())

## String count() & find() method ##
message = "Hello World"
print(message.count('l'))

Output: 3 --> Since we have 3 `l` in the "Hello World"

message = "Hello World"
print(message.find('World'))

`output`: 6 -->  World starts sixth index variable in our string

## String replace() method ##

message = "Hello World"
message = message.replace('World', 'python' )
print(message)

`output`: Hello python

## String concatenation ##

greeting = "Hello"
name = "Viswa"
message = greeting + ', ' + name + '. Welcome'
print(message)

`Output:` Hello, Viswa. Welcome

## String formatting (placeholders and format method) ##

greeting = "Hello"
name = "Viswa"
message = '{}, {} . Welcome!' .format(greeting, name)
print(message)

`Output:` Hello, Viswa. Welcome

## String formatting using Python 3.6 new f' strings ##

greeting = "Hello"
name = "Viswa"
message = f'{greeting}, {name.upper()} . Welcome!'
print(message)

`Output:` Hello, VISWA . Welcome!

## Using dir() function to print out all methods and attributes of string ##

greeting = "Hello"
name = "Viswa"
print(dir(name))

`Output:` ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',] etc.

## Using help(str) function to access a lot more info about string methods ##

greeting = "Hello"
name = "Viswa"
print(help(str.lower))

`Output:` lower(self, /)
             Return a copy of the string converted to lowercase.

# 3. Integers & Floats #
# Arithmetic Operations #
1. Addition:       3 + 2
2. Subtraction:    3 - 2
3. Multiplication: 3 * 2
4. Division:       3 / 2
5. Floor Division: 3 // 2
6. Exponent:       3 ** 2
7. Modulus:        3 % 2

# Comparision Operator #
1. Equal:                  3 == 2
2. Not Equal               3 != 2
3. Greater Than:           3 > 2
4. Less Than:              3 < 2
5. Greater than or Equal:  3 >= 2
6. Less or Equal:          3 <= 2

## Lists ##

lists are mutable in python. we can add, remove and change the position etc.

courses = ['history', 'physics', 'maths', 'science']

# print the courses list
print(courses)
`Output:` ['history', 'physics', 'maths', 'science']

# print the values by using length function
print(len(courses))
`Output:` 4

# print the courses by using index i.e (index will start from `0`)
print(courses[2])
`Output:` maths

# print the negitive index i.e(the negitive item always be last item in the list)
print(courses[-1])
`Output:` science

# print the out of range of index and check
print(courses[4])
`Output:` IndexError: list index out of range

# print the range of values
print(courses[0:2])
`Output:` ['history', 'physics']

# print the range of values i.e (it's should be assume it's starts from begining same result as above)
print(courses[:2])
`Output:` ['history', 'physics']

# print the range of values i.e (it's should start from 2 and all the way to end)
print(courses[2:])
`Output:` ['maths', 'science']

# list methods i.e (it's added in the end of the list)
courses = ['history', 'physics', 'maths', 'science']
courses.append('arts')
print(courses)

`Output:` ['history', 'physics', 'maths', 'science', 'arts']

# list methods by using insert i.e it's should be placed in first since we have added 0
courses = ['history', 'physics', 'maths', 'science']
courses.insert(0, 'arts')
print(courses)

`Output:` ['arts', 'history', 'physics', 'maths', 'science']

# list methods by using extend method
courses = ['history', 'physics', 'maths', 'science']
courses_2 = ['arts', 'education']

courses.insert(0, courses_2)
print(courses)

`Output:` [['arts', 'education'], 'history', 'physics', 'maths', 'science']

# One more xample for extend method i.e (from actual list and extend list)
courses = ['history', 'physics', 'maths', 'science']
courses_2 = ['arts', 'education']

courses.insert(0, courses_2)
print(courses[0])

`Output:` ['arts', 'education']

# One more example of extend method
courses = ['history', 'physics', 'maths', 'science']
courses_2 = ['arts', 'education']

courses.extend(courses_2)
print(courses)

`Output:` ['history', 'physics', 'maths', 'science', 'arts', 'education']

# remove some items form the list by using remove method
courses = ['history', 'physics', 'maths', 'science']
courses.remove('maths')
print(courses)

`Output:` ['history', 'physics', 'science']

# Use pop method to remove the items form list
courses = ['history', 'physics', 'maths', 'science']
courses.pop()
print(courses)

`Output:` ['history', 'physics', 'maths']

# Use reverse method to list the items
courses = ['history', 'physics', 'maths', 'science']
courses.reverse()
print(courses)

`Output:` ['science', maths', 'physics', 'history',]

# Use sort method it will trigger alphabitical order
courses = ['history', 'physics', 'maths', 'science']
courses.sort()
print(courses)

`Output:` ['history', 'maths', 'physics', 'science']

# Sort method by using numbers i.e(Ascending order)
numbers = [1, 7, 3, 5, 2]
numbers.sort()
print(numbers)

`Output:` [1, 2, 3, 5, 7]

## Tuples ##

Tuples are immutable in python. tuples are exactly the same as lists, but instaed of using squre braces [] use Parentheses ()

`Example:` tuple_1 = ('history', 'physics', 'maths', 'science')

# tuples usecase
tuple_1 = ('history', 'physics', 'maths', 'science')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

`Output:` ('history', 'physics', 'maths', 'science')
          ('history', 'physics', 'maths', 'science')

# tuples are immutable
tuple_1 = ('history', 'physics', 'maths', 'science')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'art'

print(tuple_1)
print(tuple_2)

`Output:` TypeError: 'tuple' object does not support item assignment, `beacuse tuple is immutable`

