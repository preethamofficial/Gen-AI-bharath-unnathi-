import json
from pathlib import Path
from generator import generate_study_guide


def build_html(notes: str, output: str = "outputs/study_guide.html") -> str:
    guide = generate_study_guide(notes)
    Path(output).parent.mkdir(exist_ok=True)
    cards = "".join(f"<li><b>{c['front']}</b><br>{c['back']}</li>" for c in guide.flashcards)
    quiz = "".join(f"<li>{q['question']}<br><small>{q['answer']}</small></li>" for q in guide.quiz)
    html = f"""<!doctype html><html><head><title>AI Study Guide</title><style>
body{{font-family:Arial;margin:0;background:#101418;color:#f6f7fb}}main{{max-width:900px;margin:auto;padding:32px}}
section{{border-top:1px solid #34404c;padding:20px 0}}button{{padding:10px 14px}}
</style></head><body><main><h1>AI Study Guide</h1><section><h2>Summary</h2><p>{guide.summary}</p></section>
<section><h2>Flashcards</h2><ul>{cards}</ul></section><section><h2>Quiz</h2><ol>{quiz}</ol></section>
<script>localStorage.setItem('study-guide', {json.dumps(json.dumps(guide.__dict__))});</script></main></body></html>"""
    Path(output).write_text(html, encoding="utf-8")
    return output


if __name__ == "__main__":
    print(build_html(Path("sample_notes.txt").read_text(encoding="utf-8") if Path("sample_notes.txt").exists() else input("Paste notes: ")))
