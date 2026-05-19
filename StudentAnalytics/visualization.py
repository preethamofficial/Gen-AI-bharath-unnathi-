from pathlib import Path
import matplotlib.pyplot as plt
from student import Student


def create_bar_chart(student: Student, output: str = "reports/performance.png") -> str:
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    subjects = list(student.grades)
    values = [student.subject_average(subject) for subject in subjects]
    plt.figure(figsize=(8, 4))
    plt.bar(subjects, values, color="#2f80ed")
    plt.ylim(0, 100)
    plt.title(f"{student.name} Performance")
    plt.tight_layout()
    plt.savefig(output)
    plt.close()
    return output
