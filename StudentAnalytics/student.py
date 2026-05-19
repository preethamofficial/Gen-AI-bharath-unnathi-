from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Student:
    name: str
    grades: dict[str, list[float]]
    attendance: float = 100.0
    student_id: str = field(default_factory=lambda: f"STU-{uuid4().hex[:8].upper()}")

    def subject_average(self, subject: str) -> float:
        values = self.grades.get(subject, [])
        return round(sum(values) / len(values), 2) if values else 0.0

    def gpa(self) -> float:
        averages = [self.subject_average(subject) for subject in self.grades]
        return round(sum(averages) / max(len(averages), 1) / 10, 2)

    def overall_percentage(self) -> float:
        averages = [self.subject_average(subject) for subject in self.grades]
        return round(sum(averages) / max(len(averages), 1), 2)
