from agents import analyze_sentiment, classify_email, generate_reply, proofread


def process_email(text: str) -> dict:
    draft = generate_reply(text)
    return {
        "classification": classify_email(text),
        "sentiment": analyze_sentiment(text),
        "reply": proofread(draft),
    }


if __name__ == "__main__":
    print(process_email(input("Email text: ")))
