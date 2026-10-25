# Student information: ID, name, marks
students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],
]


# Task 1: Calculate average
def calculate_average(marks):
    if not marks:
        return None
    for m in marks:
        if m < 0 or m > 100:
            return None
    return sum(marks) / len(marks)


# Task 2: Classify performance
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


# Task 3: Display report
def display_report(students):
    if not students:
        print("No student records.")
        return
    for s in students:
        avg = calculate_average(s[2])
        category = classify_performance(avg)
        if avg is None:
            print(s[0], s[1], "---", category)
        else:
            print(s[0], s[1], round(avg, 2), category)


# Test the functions
if __name__ == "__main__":
    print("Student Report")
    display_report(students)

    test_students = [
        [206, "Karim", [70, 70, 70]],
        [207, "Sadia", [60, 80, 70]],
        [208, "Bad", [50, 120, 60]],
        [209, "Empty", []],
    ]

    print("Testing extra student records")
    display_report(test_students)

    print("Testing empty student list")
    display_report([])