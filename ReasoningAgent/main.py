import json
import time
from pathlib import Path

from agents.judge_agent import judge
from agents.solver_agent import solve
from agents.verifier_agent import verify


MEMORY = Path("memory/reasoning_history.json")


def run_agent(puzzle: str) -> dict:
    start = time.perf_counter()
    solution = solve(puzzle)
    verification = verify(puzzle, solution)
    verdict = judge(solution, verification)
    verdict["response_time_ms"] = round((time.perf_counter() - start) * 1000, 2)
    MEMORY.parent.mkdir(exist_ok=True)
    history = json.loads(MEMORY.read_text(encoding="utf-8")) if MEMORY.exists() else []
    history.append({"puzzle": puzzle, "solution": solution, "verification": verification, "verdict": verdict})
    MEMORY.write_text(json.dumps(history, indent=2), encoding="utf-8")
    return verdict


if __name__ == "__main__":
    print(run_agent(input("Puzzle: ")))
