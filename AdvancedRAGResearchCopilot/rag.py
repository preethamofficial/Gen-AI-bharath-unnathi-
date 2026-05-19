from __future__ import annotations

import math
from collections import Counter


def chunk_text(text: str, size: int = 500) -> list[str]:
    words = text.split()
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)] or [text]


def score(query: str, chunk: str) -> float:
    q = Counter(query.lower().split())
    c = Counter(chunk.lower().split())
    overlap = sum(min(q[word], c[word]) for word in q)
    return round(overlap / math.sqrt(max(sum(c.values()), 1)), 4)


def retrieve(query: str, documents: list[str], top_k: int = 3) -> list[dict]:
    chunks = [(doc_id, chunk) for doc_id, doc in enumerate(documents) for chunk in chunk_text(doc, 120)]
    ranked = sorted(([{"source": doc_id, "chunk": chunk, "score": score(query, chunk)} for doc_id, chunk in chunks]), key=lambda x: x["score"], reverse=True)
    return ranked[:top_k]


def answer(query: str, documents: list[str]) -> dict:
    sources = retrieve(query, documents)
    evidence = " ".join(item["chunk"] for item in sources if item["score"] > 0)
    response = evidence[:600] if evidence else "No strong source match found."
    return {"answer": response, "citations": sources}
