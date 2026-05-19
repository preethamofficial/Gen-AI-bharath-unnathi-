# Advanced RAG Research Copilot

Lightweight retrieval-augmented research assistant with chunking, scoring, source citations, and hallucination-aware no-match behavior.

## What this project does

This tool answers research questions by searching through text documents and returning the best matching content. It does not use an online AI model; instead, it relies on the documents you provide and a simple retrieval algorithm.

## How it works

1. The script loads all `.txt` files from a `documents/` folder.
2. Each document is split into smaller chunks so the tool can compare query words more accurately.
3. It scores each chunk based on how many words overlap with the question.
4. The top matching chunks are returned as the answer and citations.
5. If no chunk scores well enough, it returns a clear no-match message.

## Setup

There are no extra dependencies beyond Python. On Windows, use the Python launcher:

```powershell
py -3 main.py
```

## Usage

1. Open a terminal in `AdvancedRAGResearchCopilot`
2. Run:

```powershell
py -3 main.py
```

3. When prompted, type your research question and press Enter.
4. Review the answer and cited source chunks.

Example question:

```text
What is RAG?
```

## Add your own documents

Create a folder named `documents` inside `AdvancedRAGResearchCopilot`, then add text files like `topic1.txt`, `topic2.txt`, etc. The program will automatically read all `.txt` files in that folder.

## Example command

```powershell
cd 'C:\Users\preet\OneDrive\Desktop\internship projects\AdvancedRAGResearchCopilot'
py -3 main.py
```

## Notes

- Use `py -3` on Windows when `python` is not available.
- The tool is useful for quick document-based research and citation-style answers.
- Better results come from adding focused documents that match the questions you want to ask.
