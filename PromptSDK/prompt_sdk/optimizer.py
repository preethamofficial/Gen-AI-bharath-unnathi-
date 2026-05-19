def optimize_prompt(prompt: str) -> str:
    checklist = "\n\nReturn: concise answer, assumptions, and verification notes."
    return prompt.strip() + checklist


def evaluate_prompt(prompt: str, response: str) -> dict:
    return {
        "clarity": min(10, max(1, len(prompt.split()) // 8)),
        "specificity": 8 if any(word in prompt.lower() for word in ["format", "criteria", "steps"]) else 5,
        "response_length": len(response.split()),
    }


def benchmark_prompt(prompt: str, responses: list[str]) -> dict:
    scores = [evaluate_prompt(prompt, response)["specificity"] for response in responses]
    return {"average_score": round(sum(scores) / max(len(scores), 1), 2), "runs": len(responses)}
