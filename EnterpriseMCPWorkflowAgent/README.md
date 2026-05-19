# Enterprise MCP Workflow Agent

Context-aware document workflow for clause extraction, risk scoring, audit state, and email generation.

## What it does

This tool analyzes enterprise documents and returns:
- Clause extraction (key contractual terms)
- Risk scoring (potential legal/business risks)
- Audit state tracking
- Auto-generated email summaries

## How it works

1. Document text is parsed through the WorkflowContext
2. Analysis extracts important clauses and identifies risks
3. Risk scoring evaluates potential impact
4. Email generator creates a summary for stakeholders
5. Audit trail tracks all processing steps

## Run

From the `EnterpriseMCPWorkflowAgent` folder:

```powershell
py -3 main.py
```

Then paste document text when prompted. The system analyzes it and generates a report plus email summary.

## Example

```text
Input: Contract clause about payment terms
Output: {
  "clauses": [...],
  "risk_score": 0.65,
  "email_summary": "This contract includes..."
}
```

## Notes

- No external dependencies required for core functionality
- Use `py -3` on Windows if `python` is not available
- Best for legal/enterprise document analysis
