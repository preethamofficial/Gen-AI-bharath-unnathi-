# AI Email Automation Agent

Multi-step email assistant for classification, urgency, spam scoring, sentiment analysis, and smart reply drafting.

## What it does

This tool processes incoming email text and returns:
- Email classification (spam, urgent, normal, etc.)
- Sentiment analysis (positive, negative, neutral)
- Auto-generated smart reply draft
- Proofread version of the reply

## How it works

1. Input email text is passed to classification agent
2. Sentiment analysis examines emotional tone
3. Reply generation creates a contextual response
4. Proofread agent checks grammar and clarity
5. Results are returned as a structured dictionary

## Run

From the `EmailAutomationAgent` folder:

```powershell
py -3 main.py
```

Then enter email text when prompted and review the classification, sentiment, and suggested reply.

## Example

```text
Input: "I'm frustrated with the delayed shipment"
Output: {
  "classification": "urgent",
  "sentiment": "negative",
  "reply": "Thank you for bringing this to our attention. We sincerely apologize for the delay and will investigate immediately."
}
```

## Notes

- No external dependencies required for core functionality
- Use `py -3` on Windows if `python` is not available
