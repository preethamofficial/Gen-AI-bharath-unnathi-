# Multi-Agent AI Debate Ecosystem

Autonomous debate flow with proponent, opponent, fact checker, and judge agents. Includes timeline and confidence scoring.

## What it does

This tool runs a structured debate with:
- **Proponent**: argues for the topic with benefits
- **Opponent**: argues against with potential harms
- **Fact Checker**: validates claims and rates confidence
- **Judge**: evaluates both sides and renders a verdict

## How it works

1. Topic is provided by user
2. Proponent agent generates supporting arguments
3. Opponent agent generates opposing arguments
4. Fact checker evaluates credibility and confidence
5. Judge reviews all arguments and renders balanced verdict
6. Full debate timeline with scores is returned

## Run

From the `MultiAgentAIDebateEcosystem` folder:

```powershell
py -3 main.py
```

Then enter a debate topic when prompted (e.g., "Should AI be used in healthcare?").

## Example Output

```json
{
  "topic": "AI in healthcare",
  "timeline": ["Pro argument...", "Con argument..."],
  "fact_check": {"confidence": 0.74},
  "verdict": {"winner": "balanced", "reason": "Both sides raised valid points"}
}
```

## Notes

- No external dependencies required
- Use `py -3` on Windows if `python` is not available
- Designed for exploring multiple perspectives on topics
