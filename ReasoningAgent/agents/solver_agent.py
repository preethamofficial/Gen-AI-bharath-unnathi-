def solve(puzzle: str) -> dict:
    answer = "Need more structured rules."
    if "all men are mortal" in puzzle.lower() and "socrates" in puzzle.lower():
        answer = "Socrates is mortal."
    return {"agent": "solver", "answer": answer, "confidence": 0.72}
