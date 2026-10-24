# ============================================
# Lab 05 - Exercise 2: Student Marks Investigator
# File: student_report.py
# ============================================

# Each student = [ID, name, [marks in 3 assessments]]
students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],
]


# -------- Task 1 --------
def calculate_average(marks):
    """Return average of marks. Return None if empty or invalid."""
    if not marks:
        return None
    for m in marks:
        if m < 0 or m > 100:
            return None
    return sum(marks) / len(marks)


# -------- Task 2 --------
def classify_performance(average):
    """Return performance category based on average."""
    if average is None:
        return "Invalid Data"
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


# -------- Task 3 --------
def display_report(students):
    """Display each student's ID, name, average, and category."""
    if not students:
        print("No student records.")
        return

    print(f"{'ID':<6}{'Name':<10}{'Average':<10}{'Category'}")
    print("-" * 45)

    for s in students:
        sid, name, marks = s
        avg = calculate_average(marks)
        cat = classify_performance(avg)

        if avg is None:
            print(f"{sid:<6}{name:<10}{'---':<10}{cat}")
        else:
            print(f"{sid:<6}{name:<10}{avg:<10.2f}{cat}")


# -------- Main / Testing --------
if __name__ == "__main__":
    print("=== Original Student Report ===")
    display_report(students)

    # ----- Testing & Debugging cases -----
    print("\n=== Testing & Debugging ===")

    test_students = [
        [206, "Karim", [70, 70, 70]],   # equal-marks / tied average
        [207, "Sadia", [60, 80, 70]],   # tied average with Karim
        [208, "Bad",   [50, 120, 60]],  # invalid mark (> 100)
        [209, "Empty", []],             # no marks
    ]

    print("\n[Test] Extra cases (tied, invalid, empty):")
    display_report(test_students)

    # Empty student list test
    print("\n[Test] Empty student list:")
    display_report([])