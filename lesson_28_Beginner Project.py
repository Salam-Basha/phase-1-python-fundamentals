# ==========================================
# Project: Student Grade Management System
# ==========================================

# Get student information
name = input("Enter student name: ")

# Get subject marks
maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
physics = int(input("Enter Physics marks: "))

# Validate marks
if (maths < 0 or maths > 100 or
    python < 0 or python > 100 or
    physics < 0 or physics > 100):

    print("\nInvalid marks! Enter marks between 0 and 100.")

else:
    # Calculate total and average
    total = maths + python + physics
    avg = total / 3

    # Determine grade
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "Fail"

    # Display student report
    print("\n========== STUDENT REPORT ==========")
    print(f"Student Name : {name}")
    print(f"Maths Marks  : {maths}")
    print(f"Python Marks: {python}")
    print(f"Physics Marks: {physics}")
    print("------------------------------------")
    print(f"Total Marks  : {total}/300")
    print(f"Average      : {avg}%")
    print(f"Grade        : {grade}")
    print("====================================")
