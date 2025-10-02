'''
condition = True
x = 10

if condition:
    print("Condition is True")
elif x > 0:
    print("x is positive")
else:
    print("Condition is False")
'''

'''
I have 5 instructors teaching courses.
'''

print ("Instructors selector software")

code = input("Enter the course code: ").strip().upper()
season = input("Enter the season (Fall, Winter, Spring, Summer): ").strip().capitalize()
year = int(input("Enter the year (e.g., 2024): ").strip())
section = input("Enter the section (A, B, C): ").strip().upper()

if code == "CS101":
    if season == "Fall" and year == 2024:
        if section == "A":
            print("Instructor: Dr. Smith")
        elif section == "B":
            print("Instructor: Prof. Johnson")
        else:
            print("No instructor assigned for this section.")
    elif season == "Winter" and year == 2024:
        if section == "A":
            print("Instructor: Dr. Brown")
        else:
            print("No instructor assigned for this section.")
    else:
        print("No courses available for this season and year.")
elif code == "MATH201":
    if season == "Spring" and year == 2024:
        if section == "A":
            print("Instructor: Dr. Taylor")
        elif section == "B":
            print("Instructor: Prof. Anderson")
        else:
            print("No instructor assigned for this section.")
    else:
        print("No courses available for this season and year.")
else:
    print("Course code not recognized.")