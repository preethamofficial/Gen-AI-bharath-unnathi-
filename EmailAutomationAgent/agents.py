def classify_email(text: str) -> dict:
    lowered = text.lower()
    urgent = any(word in lowered for word in ["urgent", "asap", "today", "deadline"])
    spam = any(word in lowered for word in ["lottery", "winner", "free money"])
    return {"urgency": "high" if urgent else "normal", "spam_probability": 0.85 if spam else 0.08, "intent": "meeting" if "meet" in lowered else "general"}


def analyze_sentiment(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ["angry", "disappointed", "issue"]):
        return "negative"
    if any(word in lowered for word in ["thanks", "great", "happy"]):
        return "positive"
    return "neutral"


def generate_reply(text: str) -> str:
    label = classify_email(text)
    prefix = "I’ll prioritize this today." if label["urgency"] == "high" else "Thanks for the update."
    return f"{prefix} I have reviewed your message and will follow up with the next steps."


def proofread(reply: str) -> str:
    return reply.strip()
