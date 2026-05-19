# Prompt Engineering SDK

Reusable prompt templates, prompt optimization, evaluation metrics, and FastAPI endpoints.

## What it does

This SDK provides tools for:
- Prompt optimization and refinement
- Prompt evaluation metrics
- Benchmark scoring
- REST API endpoints for prompt engineering tasks

## How it works

1. **Optimization**: Takes a prompt and adds structured checklist for better responses
2. **Evaluation**: Scores prompts on clarity, specificity, and detail level
3. **Benchmarking**: Tests multiple responses and averages quality scores
4. **FastAPI Server**: Exposes `/optimize` and `/evaluate` endpoints

## Setup

From the `PromptSDK` folder:

```powershell
py -3 -m pip install -r requirements.txt
```

## Run (FastAPI Server)

```powershell
cd api
py -3 -m uvicorn main:app --reload
```

Server runs on `http://localhost:8000`

## API Endpoints

### POST /optimize

```json
{"prompt": "Write a function to sort an array"}
```

Returns optimized prompt with added structure.

### POST /evaluate

```json
{"prompt": "List all Python data types", "response": "Lists 5 types..."}
```

Returns clarity, specificity, and response length scores.

## Run (Python Only)

If you don't want the FastAPI server:

```powershell
py -3
>>> from prompt_sdk.optimizer import optimize_prompt, evaluate_prompt
>>> optimize_prompt("Your prompt here")
```

## Notes

- Uses `py -3` on Windows if `python` is not available
- Requires FastAPI and uvicorn for API server
- Can be used as Python module or REST API
