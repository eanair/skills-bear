#!/usr/bin/env python3
"""
Bear Skill Example: Daily Note Creation

Daily note templates that can be auto-generated.
"""

import sys
sys.path.insert(0, '../scripts')
from bear import create_note, add_text
from datetime import date, datetime, timedelta


def create_daily_standup():
    """Daily standup note"""
    print("Example 1: Daily standup note")

    today = date.today().strftime("%Y-%m-%d")

    standup_text = """## Daily Standup - {}

### Yesterday
- [ ] Task 1: (Completed/In Progress/Blocked)
- [ ] Task 2: (Completed/In Progress/Blocked)

### Today
- [ ] Task 1: Planned completion time
- [ ] Task 2: Planned completion time
- [ ] Task 3: Planned completion time

### Blockers
- (None) or (List any blockers)

### Notes
- Team status: All good
- No critical issues
""".format(today)

    create_note(
        title=f"Daily Standup - {today}",
        text=standup_text,
        tags="standup,daily",
        add_timestamp=True
    )

    print(f"'{today}' standup note created\n")


def create_daily_journal():
    """Daily journal"""
    print("Example 2: Daily journal")

    today = date.today().strftime("%Y-%m-%d")
    day_name = date.today().strftime("%A")

    journal_text = f"""# Daily Journal - {today} ({day_name})

## Morning Reflection
- How are you feeling today?
- What's your top priority?
- Any concerns or worries?

## Throughout the Day
### Highlights
- Great moment:
- Accomplishment:
- Positive interaction:

### Challenges
- Difficulty faced:
- How you handled it:
- Learning:

## Evening Reflection
- What went well today?
- What could be improved?
- Gratitude (3 things):
  1.
  2.
  3.

## Tomorrow
- One goal for tomorrow:
- Key focus area:
- Self-care activity:

---
*End of Day - {datetime.now().strftime('%H:%M:%S')}*
"""

    create_note(
        title=f"Daily Journal - {today}",
        text=journal_text,
        tags="journal,daily,personal",
        add_timestamp=True
    )

    print(f"'{today}' journal created\n")


def create_daily_log():
    """Daily log"""
    print("Example 3: Daily log")

    today = date.today().strftime("%Y-%m-%d")

    log_text = f"""# Daily Log - {today}

## Work
- Morning meeting: [Time]
- Focus session: [Task]
- Email/Communication: [Summary]
- Meetings/Calls: [Count and summary]

## Personal
- Exercise: [None/Activity]
- Meals: Breakfast/Lunch/Dinner
- Sleep: [Hours]

## Learning
- Read: [Article/Book]
- Watched: [Video/Tutorial]
- Practiced: [Skill]

## Metrics
- Lines of code written: ?
- Meetings attended: ?
- Emails processed: ?
- Tasks completed: ?

## Tomorrow's Focus
- [ ] Priority 1
- [ ] Priority 2
- [ ] Priority 3
"""

    create_note(
        title=f"Daily Log - {today}",
        text=log_text,
        tags="log,daily,tracking",
        add_timestamp=True
    )

    print(f"'{today}' log created\n")


def create_weekly_review():
    """Weekly review"""
    print("Example 4: Weekly review")

    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).strftime("%Y-%m-%d")
    week_num = today.strftime("%W")

    review_text = f"""# Weekly Review - Week {week_num}

## Accomplishments
- [ ] Goal 1: Achievement level (1-10)
- [ ] Goal 2: Achievement level (1-10)
- [ ] Goal 3: Achievement level (1-10)

## This Week's Highlights
- Major achievement:
- Best moment:
- Most productive day:

## Challenges & Solutions
- Challenge 1: Solution:
- Challenge 2: Solution:
- Challenge 3: Solution:

## Metrics & Numbers
- Tasks completed: ?
- Hours worked: ?
- Focus sessions: ?
- Meetings: ?

## Next Week's Goals
- [ ] Priority 1
- [ ] Priority 2
- [ ] Priority 3
- [ ] Priority 4

## Learning & Growth
- Learned:
- Improved:
- To practice:

## Personal Reflection
- Energy level: [1-10]
- Stress level: [1-10]
- Satisfaction: [1-10]
- Self-care: [Yes/No]

## Notes & Adjustments
- Process improvements:
- Time management:
- Work-life balance:

---
*Week {week_num} Review - {today.strftime('%Y-%m-%d')}*
"""

    create_note(
        title=f"Weekly Review - Week {week_num}",
        text=review_text,
        tags="review,weekly,planning",
        add_timestamp=True
    )

    print(f"Weekly review note created\n")


def create_daily_with_categories():
    """Daily note with categories"""
    print("Example 5: Daily note with categories")

    today = date.today().strftime("%Y-%m-%d")

    detailed_text = f"""# Daily Overview - {today}

## Work
### Morning
- [ ] Check emails
- [ ] Review calendar
- [ ] Plan day

### Afternoon
- [ ] Deep work session: [Topic]
- [ ] Team collaboration
- [ ] Review progress

### Evening
- [ ] Wrap up tasks
- [ ] Plan tomorrow
- [ ] Update status

## Health & Fitness
- Exercise: [Type/Duration]
  - Completed: Yes/No
  - Energy: [1-10]
  - Notes:

## Learning
- Study session: [Topic/Duration]
  - Resources:
  - Key learnings:

## Personal Development
- Reflection time: [Duration]
- Meditation/Mindfulness: [Yes/No]
- Growth area:

## Relationships
- Family time: [Yes/No]
- Friends: [Contacted/Met]
- Meaningful interaction:

## Habits Tracked
- [ ] Morning routine completed
- [ ] Water intake (8 glasses)
- [ ] Healthy meals
- [ ] Bedtime on schedule
- [ ] No phone 1 hour before bed

## Tomorrow's Preparation
- [ ] Review priorities
- [ ] Prepare materials
- [ ] Set intentions
- [ ] Plan schedule

---
*Logged: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

    create_note(
        title=f"Daily Overview - {today}",
        text=detailed_text,
        tags="daily,overview,comprehensive",
        add_timestamp=True
    )

    print(f"Comprehensive daily note created\n")


def create_consecutive_days():
    """Create notes for consecutive days"""
    print("Example 6: Create notes for consecutive days")

    print("Create notes for the next 7 days? (Y/n)")
    response = input().strip().lower()

    if response == 'n':
        print("Cancelled\n")
        return

    for i in range(7):
        date_obj = date.today() + timedelta(days=i)
        date_str = date_obj.strftime("%Y-%m-%d")
        day_name = date_obj.strftime("%A")

        template = f"""# Daily Plan - {date_str} ({day_name})

## Morning Routine
- [ ] 6:00 AM Wake up
- [ ] 6:15 AM Exercise
- [ ] 6:45 AM Shower
- [ ] 7:00 AM Breakfast

## Work Focus
- [ ] Priority 1:
- [ ] Priority 2:
- [ ] Priority 3:

## Evening
- [ ] Reflection
- [ ] Prepare tomorrow
- [ ] Bedtime routine

## Notes
(Add daily notes here)
"""

        create_note(
            title=f"Daily Plan - {date_str}",
            text=template,
            tags="daily,planning,schedule"
        )

        if i == 0:
            print(f"  {date_str} note created")
        else:
            print(f"  {date_str} note created")

    print("\nAll 7 days of notes created\n")


if __name__ == "__main__":
    print("Bear Skill - Daily Note Creation Examples\n")
    print("=" * 50)
    print()

    create_daily_standup()
    create_daily_journal()
    create_daily_log()
    create_weekly_review()
    create_daily_with_categories()
    create_consecutive_days()

    print("=" * 50)
    print("All daily note examples completed!")
    print("\nTips:")
    print("- This script can be run with Cron or automation tools")
    print("- Modify templates to suit your needs")
    print("- Use tags to categorize notes for easier searching")
    print("- Use add_timestamp=True to automatically record creation time")
