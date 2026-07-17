def analyze_result(name, roll, marks):
    # Calculate total and average
    total = sum(marks)
    average = total / len(marks)

    # Assign grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Display student details
    print("\nStudent:", name, "(Roll:", roll, ")")
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

    # Print subjects with marks below 40
    print("Subjects below 40:", end=" ")
    found = False
    for i in range(len(marks)):
        if marks[i] < 40:
            print("Subject", i + 1, end=" ")
            found = True

    if not found:
        print("None")
    else:
        print()


# -------- Main Program --------
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

marks = []
print("Enter marks for 5 subjects:")
for i in range(5):
    mark = float(input(f"Subject {i + 1}: "))
    marks.append(mark)

# Call the function
analyze_result(name, roll, marks)