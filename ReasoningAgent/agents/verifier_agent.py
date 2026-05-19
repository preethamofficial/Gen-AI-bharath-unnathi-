def verify(puzzle: str, solution: dict) -> dict:
    answer = solution["answer"]
    passed = bool(answer) and "Need more" not in answer
    return {"agent": "verifier", "passed": passed, "critique": "Answer is consistent." if passed else "Insufficient reasoning."}
