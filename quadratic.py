a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions (all x are solutions).")
        else:
            print("No solution.")
    else:
        x = -c / b
        print(f"Linear equation solution: x = {x}")

else:
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        print(f"Two distinct real roots: x1 = {root1}, x2 = {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"One real root: x = {root}")
    else:
        real = -b / (2*a)
        imaginary = (-discriminant**0.5) / (2*a)
        print(f"Two complex roots: x1 = {real} + {imaginary}i, x2 = {real} - {imaginary}i")