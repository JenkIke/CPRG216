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

year_of_birth = int(input("Please enter your year of birth\n"))
Month_of_birth = int(input("Please enter your month of birth (1-12)\n"))
if Month_of_birth > 9:
    print("Your age is", 2024 - year_of_birth)
else:
    print("Your age is", 2025 - year_of_birth)