from dataclasses import dataclass


@dataclass
class StudyGuide:
    summary: str
    flashcards: list[dict[str, str]]
    quiz: list[dict[str, str]]
    weak_topics: list[str]


def generate_study_guide(notes: str) -> StudyGuide:
    sentences = [s.strip() for s in notes.replace("\n", " ").split(".") if s.strip()]
    keywords = sorted({word.strip(",;:").lower() for word in notes.split() if len(word) > 6})[:8]
    return StudyGuide(
        summary=". ".join(sentences[:3]) + ("." if sentences else ""),
        flashcards=[{"front": f"What is {word}?", "back": f"Review the section about {word}."} for word in keywords],
        quiz=[{"question": f"Explain {word}.", "answer": f"Use notes to explain {word}."} for word in keywords[:5]],
        weak_topics=keywords[-3:],
    )
