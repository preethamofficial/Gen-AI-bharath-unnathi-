# AI Study Guide Ecosystem

Generates summaries, flashcards, quizzes, weak-topic hints, and a responsive HTML dashboard.

## What it does

This tool transforms study notes into interactive study materials:
- Generates concise summaries
- Creates flashcard questions and answers
- Generates practice quizzes
- Identifies weak topics needing review
- Outputs interactive HTML dashboard

## How it works

1. Input study notes or paste text
2. Generator module analyzes and organizes content
3. Creates summary of key points
4. Generates flashcards with front/back format
5. Creates quiz questions with answers
6. Identifies topics needing more study
7. Outputs HTML dashboard with all materials
8. Study data stored in localStorage for offline access

## Run

From the `StudyGuideEcosystem` folder:

```powershell
py -3 app.py
```

Then paste study notes when prompted (or create `sample_notes.txt` file).

## Output

Generates `outputs/study_guide.html` with:
- Summary section
- Flashcard deck
- Practice quiz
- Interactive dashboard

## Example

```text
Input: Study notes on photosynthesis
Output: HTML file with summary, 10+ flashcards, 5 quiz questions
```

## Notes

- Uses `py -3` on Windows if `python` is not available
- HTML dashboard responsive and works offline
- Data stored in browser localStorage
