# This is the third in class demo #


# Review

# 4 primitive types in python, string, boolean, int, float


'''
w = "word"
x = 1
y = 2.5
z = True


print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(type(print))
print(type(print()))
'''


# some functions call : print, input, int, float, str, bool

'''
num_as_text = "43"
num_as_num = int(num_as_text)

print(num_as_text)

print(num_as_num)
print(str(num_as_num)) # same thing, python casts with print statement
'''

# Using the input function, input function always returns a string (text)
'''
year_of_birth = int(input("Please enter your year of birth\n"))
Month_of_birth = int(input("Please enter your month of birth (1-12)\n"))
if Month_of_birth > 9:
    print("Your age is", 2024 - year_of_birth)
else:
    print("Your age is", 2025 - year_of_birth)
'''

# print function with seperators

print("Hello", "world", "this", "is", "a", "test", sep="***", end="\n")

# \n is a new line, \t is a tab

print("Hello\nworld\nthis\nis\na\ntest")
print("Hello\tworld\tthis\tis\ta\ttest")

# these are called escape characters, they allow you to do special things in strings with a backslash
# \n, \t, \', \", \\
print('I\'m a student')
print("He said \"Hello\" to me")
print("This is a backslash: \\")

# precedence rules

expression = 3 + 4 * 5 - 6 / 2
print(expression)
#BEDMAS

complex_expression = 4/2*3
print(complex_expression)
complex_expression2 = 4/(2*3)
# in this case you must wor left to right for precedence

#More about assignment statements
x = 3
x = x + 2
print(x)
# x = 5

# augmented assignment
x += 2 # same as x = x + 2
print(x)