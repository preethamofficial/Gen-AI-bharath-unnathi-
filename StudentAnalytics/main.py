import json
from pathlib import Path

from ai_feedback import generate_feedback
from analytics import class_topper, rank_students
from student import Student
from visualization import create_bar_chart


DATA_FILE = Path("data/students.json")


def load_students() -> list[Student]:
    DATA_FILE.parent.mkdir(exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")
    return [Student(**item) for item in json.loads(DATA_FILE.read_text(encoding="utf-8"))]


def save_students(students: list[Student]) -> None:
    DATA_FILE.write_text(json.dumps([student.__dict__ for student in students], indent=2), encoding="utf-8")


def demo() -> None:
    students = load_students() or [
        Student("Asha", {"Math": [88, 91], "Physics": [72, 76], "English": [84]}, 94),
        Student("Ravi", {"Math": [70], "Physics": [68], "English": [80]}, 82),
    ]
    save_students(students)
    print("Leaderboard:", [s.name for s in rank_students(students)])
    print("Topper:", class_topper(students).name)
    print(generate_feedback(students[0]))
    print("Chart:", create_bar_chart(students[0]))


if __name__ == "__main__":
    demo()
