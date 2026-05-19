from fastapi import FastAPI
from pydantic import BaseModel
from prompt_sdk.optimizer import optimize_prompt, evaluate_prompt

app = FastAPI(title="Prompt Engineering SDK")


class PromptRequest(BaseModel):
    prompt: str
    response: str = ""


@app.post("/optimize")
def optimize(request: PromptRequest):
    return {"optimized_prompt": optimize_prompt(request.prompt)}


@app.post("/evaluate")
def evaluate(request: PromptRequest):
    return evaluate_prompt(request.prompt, request.response)
