# Internship Portfolio Projects

This repository contains 10 AI-focused portfolio projects built for research, automation, analytics, UX, and workflow experimentation.

## Projects

1. **AdvancedBankingSystem**
   - Python CLI banking app with account creation, deposits, withdrawals, transfers, transaction history, spending analysis, and JSON persistence.
   - Includes `BankAccount`, `SavingsAccount`, and `CurrentAccount` models, plus validation and logging utilities.

2. **StudentAnalytics**
   - Student grade analytics platform that computes GPA, rankings, weakest subjects, grade prediction, personalized feedback, and charts.
   - Loads student metrics from `data/students.json` and generates visual dashboards.

3. **ReasoningAgent**
   - Three-agent logical reasoning pipeline with solver, verifier, and judge components.
   - Validates answers, tracks reasoning history, and provides verdicts with confidence scoring.

4. **StudyGuideEcosystem**
   - Generates study summaries, flashcards, quizzes, and weak-topic suggestions from input notes.
   - Outputs an interactive HTML study guide and dashboard.

5. **FrontendGeneratorStudio**
   - React + Vite frontend studio for generating UI components with animation and responsive design.
   - Uses Framer Motion, Lucide icons, and hot module reloading for rapid UI exploration.

6. **PromptSDK**
   - Prompt engineering SDK for prompt optimization, evaluation, and benchmarking.
   - Includes a FastAPI server exposing `/optimize` and `/evaluate` endpoints.

7. **EmailAutomationAgent**
   - Email assistant that classifies email intent, analyzes sentiment, drafts replies, and proofreads responses.
   - Useful for automating inbox workflows and generating polite replies.

8. **EnterpriseMCPWorkflowAgent**
   - Enterprise workflow agent for document clause extraction, risk scoring, audit tracking, and summary email generation.
   - Designed for legal and business document analysis.

9. **AdvancedRAGResearchCopilot**
   - Retrieval-augmented research assistant that searches local documents, chunks text, scores relevance, and returns cited answers.
   - Great for offline research with document-based citations.

10. **MultiAgentAIDebateEcosystem**
   - Multi-agent debate system with proponent, opponent, fact checker, and judge roles.
   - Produces balanced debate timelines, claim validation, confidence scores, and verdicts.

## Running the projects

- Python projects: use `py -3` on Windows, e.g. `py -3 main.py` inside each Python project folder.
- React project: use `npm install` and `npm run dev` inside `FrontendGeneratorStudio`.
- PromptSDK API: run the FastAPI service from `PromptSDK/api` with `py -3 -m uvicorn main:app --reload`.

## Notes

- This repository is intended as a portfolio collection of AI and automation projects.
- The root contains project folders, each with its own `README.md`, source code, and data files.
- A standard `.gitignore` prevents environment folders, logs, and build artifacts from being committed.
