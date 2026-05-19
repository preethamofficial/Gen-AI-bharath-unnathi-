from dataclasses import dataclass, field
from datetime import date


@dataclass
class WorkflowContext:
    user_role: str
    document_history: list[str] = field(default_factory=list)
    current_state: str = "uploaded"


def extract_clauses(document: str) -> list[str]:
    return [line.strip() for line in document.splitlines() if any(word in line.lower() for word in ["shall", "must", "deadline", "terminate"])]


def risk_score(clauses: list[str]) -> int:
    score = 10 * len(clauses)
    score += 20 if any("terminate" in clause.lower() for clause in clauses) else 0
    return min(score, 100)


def analyze_document(document: str, context: WorkflowContext) -> dict:
    clauses = extract_clauses(document)
    context.current_state = "analyzed"
    context.document_history.append(f"analyzed:{date.today().isoformat()}")
    return {"clauses": clauses, "risk_score": risk_score(clauses), "context": context.__dict__}


def generate_email(analysis: dict) -> str:
    return f"Document review complete. Risk score: {analysis['risk_score']}. Clauses needing review: {len(analysis['clauses'])}."
