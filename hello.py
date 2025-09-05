"""
Simple program with if-else conditions.
Checks student grades and eligibility.
"""

def check_pass_fail(marks):
    """Check if the student passed or failed"""
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

def grade(marks):
    """Return grade based on marks"""
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

def scholarship_eligibility(marks, attendance):
    """Check if student is eligible for scholarship"""
    if marks >= 85 and attendance >= 90:
        return "Eligible for Scholarship"
    elif marks >= 70 and attendance >= 80:
        return "Partially Eligible"
    else:
        return "Not Eligible"

def main():
    """Main function to test conditions"""
    students = [
        {"name": "Raj", "marks": 95, "attendance": 92},
        {"name": "Shrusti", "marks": 78, "attendance": 85},
        {"name": "Pukkamal", "marks": 62, "attendance": 75},
        {"name": "Ravi", "marks": 35, "attendance": 60},
    ]

    for student in students:
        print("\nStudent:", student["name"])
        print("Marks:", student["marks"])
        print("Attendance:", student["attendance"])
        print("Pass/Fail:", check_pass_fail(student["marks"]))
        print("Grade:", grade(student["marks"]))
        print("Scholarship:", scholarship_eligibility(student["marks"], student["attendance"]))

if __name__ == "__main__":
    main()

