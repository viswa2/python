# Python Programming Guide

This guide covers fundamental Python concepts with examples. Each section includes code samples and explanations.

## Table of Contents
1. [Hello World](#hello-world)
2. [Strings](#strings)
   - [Single vs Double Quotes](#single-vs-double-quotes)
   - [Multiline Strings](#multiline-strings)
   - [String Operations](#string-operations)
   - [String Methods](#string-methods)
   - [String Formatting](#string-formatting)

## Hello World
Basic "Hello World" program implementation can be found in `01-hello-world.py`.

## Strings

### Single vs Double Quotes
When working with strings containing apostrophes, you have two options:

1. Using escape characters:
```python
# Using escape character
text = 'Viswa\'s World'
```

2. Using double quotes (recommended):
```python
# Better approach
text = "Viswa's World"
```

### Multiline Strings
Python supports multiline strings using triple double quotes:

```python
"""Viswa's World was fantastic 
in the 1990's"""
```

### String Operations

#### Length Function
```python
message = "Hello World"
print(len(message))  # Get string length
```

#### String Indexing
```python
message = "Hello World"
print(message[10])  # Outputs: 'd'
```

#### String Slicing
```python
message = "Hello World"
print(message[0:5])  # Outputs: 'Hello'
```

### String Methods

#### Case Conversion
```python
message = "Hello World"
print(message.upper())  # Convert to uppercase
print(message.lower())  # Convert to lowercase
```

#### Count and Find
```python
message = "Hello World"
print(message.count('l'))    # Outputs: 3 (counts occurrences of 'l')
print(message.find('World')) # Outputs: 6 (index where 'World' starts)
```

#### Replace
```python
message = "Hello World"
message = message.replace('World', 'Python')
print(message)  # Outputs: 'Hello Python'
```

### String Formatting

#### Basic String Concatenation
```python
greeting = "Hello"
name = "Viswa"
message = greeting + ', ' + name + '. Welcome'
# Outputs: 'Hello, Viswa. Welcome'
```

#### Format Method
```python
greeting = "Hello"
name = "Viswa"
message = '{}, {}. Welcome!'.format(greeting, name)
# Outputs: 'Hello, Viswa. Welcome!'
```

#### F-Strings (Python 3.6+)
```python
greeting = "Hello"
name = "Viswa"
message = f'{greeting}, {name.upper()}. Welcome!'
# Outputs: 'Hello, VISWA. Welcome!'
```

### Additional Information
- Use `dir()` function to view all available string methods and attributes
- Methods are similar to functions but are associated with objects

---
*Note: This guide is continuously updated with new Python concepts and examples.*

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

