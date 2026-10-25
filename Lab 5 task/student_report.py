

# Student information: ID, name, marks
students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],
]


# Calculate the average of the marks
def calculate_average(marks):
    if not marks:
        return None

    for m in marks:
        if m < 0 or m > 100:
            return None

    return sum(marks) / len(marks)


# Decide the performance category from the average
def classify_performance(average):
    if average is None:
        return "Invalid Data"
    elif average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


# Display each student's result
def display_report(students):
    if not students:
        print("No student records.")
        return

    print(f"{'ID':<6}{'Name':<10}{'Average':<10}{'Category'}")
    print("-" * 45)

    for s in students:
        sid, name, marks = s

        avg = calculate_average(marks)
        category = classify_performance(avg)

        if avg is None:
            print(f"{sid:<6}{name:<10}{'---':<10}{category}")
        else:
            print(f"{sid:<6}{name:<10}{avg:<10.2f}{category}")


# Test the functions
if __name__ == "__main__":

    print("Student Report")
    display_report(students)

    # Test students with the same average
    test_students = [
        [206, "Karim", [70, 70, 70]],
        [207, "Sadia", [60, 80, 70]],
        [208, "Bad", [50, 120, 60]],
        [209, "Empty", []],
    ]

    print("\nTesting extra student records")
    display_report(test_students)

    # Check what happens when there are no student records
    print("\nTesting empty student list")
    display_report([])