from pathlib import Path
from rag import answer


if __name__ == "__main__":
    docs = [path.read_text(encoding="utf-8") for path in Path("documents").glob("*.txt")]
    if not docs:
        docs = ["RAG combines retrieval, citations, chunking, and generation to reduce hallucinations."]
    print(answer(input("Research question: "), docs))
