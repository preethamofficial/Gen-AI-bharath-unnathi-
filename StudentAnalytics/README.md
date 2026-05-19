# AI Student Grade Analytics Platform

Analytics toolkit for GPA, ranking, weakest subject detection, grade prediction, AI-style feedback, and charts.

## What it does

This tool provides student grade analytics:
- Calculates GPA and rankings
- Identifies weakest subjects
- Predicts future grades
- Generates AI-style personalized feedback
- Creates bar charts for visualization

## How it works

1. Student data is loaded from `data/students.json`
2. Analytics module calculates rankings and GPA
3. Identifies subjects with lowest performance
4. AI feedback generator creates personalized suggestions
5. Visualization module creates charts
6. Results displayed in dashboard format

## Setup

From the `StudentAnalytics` folder:

```powershell
py -3 -m pip install -r requirements.txt
```

## Run

```powershell
py -3 main.py
```

This runs a demo showing leaderboard, class topper, AI feedback, and charts.

## Data Format

Student data in `data/students.json`:

```json
[
  {
    "name": "Asha",
    "subjects": {"Math": [88, 91], "Physics": [72, 76]},
    "gpa": 3.8
  }
]
```

## Notes

- Uses `py -3` on Windows if `python` is not available
- Student data persists automatically
- Charts are generated using matplotlib
