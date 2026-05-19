def judge(solution: dict, verification: dict) -> dict:
    return {
        "agent": "judge",
        "final_answer": solution["answer"] if verification["passed"] else "Unable to solve confidently.",
        "status": "accepted" if verification["passed"] else "needs_revision",
    }
