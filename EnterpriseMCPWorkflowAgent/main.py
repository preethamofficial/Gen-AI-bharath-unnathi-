from workflow import WorkflowContext, analyze_document, generate_email


if __name__ == "__main__":
    document = input("Paste document text: ")
    analysis = analyze_document(document, WorkflowContext(user_role="analyst"))
    print(analysis)
    print(generate_email(analysis))
