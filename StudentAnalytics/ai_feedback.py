from student import Student
from analytics import weakest_subject, predict_future_grade


def generate_feedback(student: Student) -> str:
    weak = weakest_subject(student)
    predicted = predict_future_grade(student)
    risk = "low" if predicted >= 60 else "high"
    return (
        f"{student.name}, your current GPA is {student.gpa()}. "
        f"Focus on {weak} with weekly practice. Predicted score is {predicted}%, "
        f"so pass/fail risk is {risk}."
    )
