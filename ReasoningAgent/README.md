# AI Logical Reasoning Agent

Three-agent reasoning pipeline: solver, verifier, judge. It stores memory, response time, and correction status.

## What it does

This tool solves logical reasoning puzzles through a three-stage process:
- **Solver**: attempts to solve the puzzle
- **Verifier**: validates the solution
- **Judge**: renders final verdict with confidence score

## How it works

1. User provides a logic puzzle or reasoning challenge
2. Solver agent attempts to find an answer
3. Verifier agent checks the solution's validity
4. Judge agent reviews and provides final verdict
5. Response time is measured and stored
6. Results are saved to `memory/reasoning_history.json`

## Run

From the `ReasoningAgent` folder:

```powershell
py -3 main.py
```

Then enter a logical puzzle when prompted (e.g., "All men are mortal. Socrates is a man. What can we conclude?").

## Example

```text
Input: "All men are mortal. Socrates is a man. Is Socrates mortal?"
Output: {
  "solution": "Socrates is mortal",
  "verification": "Valid through modus ponens",
  "verdict": "Correct",
  "response_time_ms": 45
}
```

## Notes

- No external dependencies required
- Uses `py -3` on Windows if `python` is not available
- Reasoning history persists in `memory/reasoning_history.json`
