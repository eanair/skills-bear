# Bear Workflows and Integration Patterns

Practical applications of Bear skill in real workflows.

## Contents

1. [Daily Workflows](#daily-workflows)
2. [Project Management](#project-management)
3. [Web Content Management](#web-content-management)
4. [Code Review Integration](#code-review-integration)
5. [Data Analysis Results](#data-analysis-results)

---

## Daily Workflows

### Auto-generate Daily Notes

Automatically create today's work note each day.

```python
from scripts.bear import create_note
from datetime import date

today = date.today().strftime("%Y-%m-%d")
create_note(
    title=f"Daily Log - {today}",
    text="""## Daily Standup

### Done
- [ ] Task 1

### In Progress
- [ ] Task 2

### Blocked
- [ ] Nothing

### Notes
-
""",
    tags="daily,log",
    add_timestamp=True
)
```

### Morning Check-in

Review your todo list and plan for the day.

```python
from scripts.bear import search_notes

results = search_notes(term="")
todo_notes = [n for n in results if "todo" in str(n.get("tags", []))]

print("Today's TODOs:")
for note in todo_notes:
    print(f"  - {note['title']}")
```

---

## Project Management

### Track Project Status

Record and manage progress for each project.

```python
from scripts.bear import create_note, search_notes, add_text

# 1. Create project status note
result = create_note(
    title="Project X - Status",
    text="""# Project X

## Current Status
- Phase: Planning
- Progress: 25%

## Milestones
- [ ] Design complete (2024-02-01)
- [ ] Development start (2024-02-15)
- [ ] Testing (2024-03-15)

## Blockers
- Waiting for design approval

## Team
- Lead: Alice
- Dev: Bob
""",
    tags="project,project-x",
    return_id=True
)

project_id = result['identifier']

# 2. Add weekly update
add_text(
    note_id=project_id,
    text="""

## Week 3 Update (2024-01-22)
- Design approved by stakeholders
- Development environment setup complete
""",
    mode="append"
)

# 3. Search project notes
results = search_notes(term="", tag="project-x")
for note in results:
    print(f"Note: {note['title']}")
```

### Tag-based Filtering

Group related notes by project tags.

```python
from scripts.bear import open_tag

# View all notes for a specific project
open_tag("project-x")

# View by priority
open_tag("priority/high")
```

---

## Web Content Management

### Save and Categorize Articles

Automatically save web content to Bear and categorize with tags.

```python
from scripts.bear import grab_url

# Save tech articles
urls = [
    "https://docs.python.org/3/library/asyncio.html",
    "https://developer.apple.com/documentation/foundation/",
    "https://github.com/trending"
]

for url in urls:
    grab_url(
        url=url,
        tags="reference,dev"
    )

print(f"Saved {len(urls)} articles.")
```

### Research Collection

Collect research materials on specific topics.

```python
from scripts.bear import grab_url

research_urls = [
    "https://example.com/market-trends",
    "https://example.com/competitor-analysis"
]

for url in research_urls:
    grab_url(
        url=url,
        tags="research,marketing,2024"
    )
```

---

## Code Review Integration

### Save Code Review Results

Automatically save code review results to Bear.

```python
from scripts.bear import create_note

review_results = {
    "file": "main.py",
    "issues": [
        "Line 42: Add error handling",
        "Line 67: Refactor duplicate code",
        "Line 89: Add type hints"
    ],
    "approved": False,
    "reviewer": "Alice"
}

review_text = f"""# Code Review: {review_results['file']}

## Reviewer
{review_results['reviewer']}

## Issues Found
{''.join(f'- {issue}\n' for issue in review_results['issues'])}

## Status
{'APPROVED' if review_results['approved'] else 'NEEDS CHANGES'}

## Comments
[Add reviewer comments here]
"""

create_note(
    title=f"Code Review - {review_results['file']}",
    text=review_text,
    tags="code-review,review-needed",
    add_timestamp=True
)
```

### Save Code Snippets

Save and categorize useful code snippets.

```python
from scripts.bear import create_note

snippet = {
    "language": "python",
    "title": "Async Context Manager",
    "code": """class AsyncResource:
    async def __aenter__(self):
        print("Resource acquired")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Resource released")
""",
    "tags": ["python", "async"]
}

create_note(
    title=f"Snippet: {snippet['title']}",
    text=f"""# {snippet['title']}

Language: {snippet['language']}

```{snippet['language']}
{snippet['code']}
```

## Use Case
[Describe when to use this pattern]

## References
- [Python docs](https://docs.python.org)
""",
    tags=",".join(snippet['tags'])
)
```

---

## Data Analysis Results

### Generate Analysis Reports

Automatically convert data analysis results into notes.

```python
from scripts.bear import create_note
import json

analysis_results = {
    "title": "Q1 2024 User Analytics",
    "metrics": {
        "total_users": 15420,
        "active_users": 8934,
        "churn_rate": 0.12,
        "avg_session_time": "8m 32s"
    },
    "insights": [
        "User growth: +23% vs Q4 2023",
        "Mobile traffic: 67% of total",
        "Peak hours: 2-4 PM EST"
    ]
}

report_text = f"""# {analysis_results['title']}

## Key Metrics

| Metric | Value |
|--------|-------|
| Total Users | {analysis_results['metrics']['total_users']:,} |
| Active Users | {analysis_results['metrics']['active_users']:,} |
| Churn Rate | {analysis_results['metrics']['churn_rate']:.1%} |
| Avg Session | {analysis_results['metrics']['avg_session_time']} |

## Insights

{''.join(f'- {insight}\n' for insight in analysis_results['insights'])}

## Recommendations

- [ ] Increase mobile experience investment
- [ ] Target peak hours for campaigns
- [ ] Investigate churn causes

## Data

```json
{json.dumps(analysis_results, indent=2)}
```
"""

create_note(
    title=analysis_results['title'],
    text=report_text,
    tags="analytics,report,q1-2024",
    add_timestamp=True
)
```

---

## Integration Tips

### Environment Variable Setup

Set the API token before running scripts:

```bash
export BEAR_API_TOKEN="your-token-here"
python3 your_script.py
```

### Error Handling

Always verify API token for operations that require it:

```python
from scripts.bear import search_notes
import os

if not os.environ.get("BEAR_API_TOKEN"):
    print("Error: BEAR_API_TOKEN not set")
    exit(1)

try:
    results = search_notes(term="python")
    print(f"Found {len(results)} notes")
except Exception as e:
    print(f"Search failed: {e}")
```

### Batch Operations

Consider performance when processing multiple notes:

```python
from scripts.bear import create_note
import time

notes_to_create = [...]

for i, note_data in enumerate(notes_to_create):
    create_note(**note_data)

    # Add delay to reduce load on Bear app
    if (i + 1) % 10 == 0:
        time.sleep(1)
        print(f"Completed {i + 1}/{len(notes_to_create)}")
```

### Working Without xcall

Operations that don't need responses work without xcall:

```python
from scripts.bear import create_note, open_tag

# No response needed - xcall not required
create_note(
    title="Quick Note",
    text="Content",
    tags="quick"
)

# Open tag - xcall not required
open_tag("work")

# Response needed - xcall required
from scripts.bear import search_notes
results = search_notes(term="python")  # Requires BEAR_API_TOKEN and xcall
```

---

## Automation Ideas

- Auto-generate daily notes with Cron
- Create notes from emails
- Auto-save RSS feeds to Bear
- Daily data collection and analysis reports
- Todo reminders and priority tracking
- Auto-generate daily journal templates
