from __future__ import annotations

from statistics import pstdev
from student import Student


def rank_students(students: list[Student]) -> list[Student]:
    return sorted(students, key=lambda item: item.overall_percentage(), reverse=True)


def class_topper(students: list[Student]) -> Student | None:
    ranked = rank_students(students)
    return ranked[0] if ranked else None


def weakest_subject(student: Student) -> str:
    return min(student.grades, key=student.subject_average)


def standard_deviation(student: Student) -> float:
    scores = [score for values in student.grades.values() for score in values]
    return round(pstdev(scores), 2) if len(scores) > 1 else 0.0


def percentile(student: Student, students: list[Student]) -> float:
    below = sum(1 for item in students if item.overall_percentage() <= student.overall_percentage())
    return round((below / max(len(students), 1)) * 100, 2)


def predict_future_grade(student: Student) -> float:
    scores = [student.subject_average(subject) for subject in student.grades]
    attendance_factor = min(student.attendance / 100, 1)
    return round((sum(scores) / max(len(scores), 1)) * (0.85 + 0.15 * attendance_factor), 2)
