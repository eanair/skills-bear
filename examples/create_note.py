#!/usr/bin/env python3
"""
Bear Skill Example: Note Creation

Demonstrates various ways to create new notes.
"""

import sys
sys.path.insert(0, '../scripts')
from bear import create_note


def example_basic_note():
    """Basic note creation"""
    print("Example 1: Basic note creation")
    create_note(
        title="My First Note",
        text="This is the content of my first note."
    )
    print("Note created\n")


def example_note_with_tags():
    """Note creation with tags"""
    print("Example 2: Note creation with tags")
    create_note(
        title="Project Planning",
        text="""# Q1 2024 Planning

## Objectives
- Launch new feature
- Improve performance
- Fix critical bugs

## Timeline
- January: Design phase
- February: Development
- March: Testing & Launch
""",
        tags="planning,2024,q1"
    )
    print("Note with tags created\n")


def example_note_with_timestamp():
    """Note creation with timestamp"""
    print("Example 3: Note creation with timestamp")
    create_note(
        title="Daily Standup",
        text="""## Yesterday
- Completed feature X
- Fixed bug in module Y

## Today
- [ ] Review pull request
- [ ] Update documentation

## Blockers
None
""",
        tags="standup,daily",
        add_timestamp=True
    )
    print("Note with timestamp created\n")


def example_note_with_response():
    """Get note ID from response"""
    print("Example 4: Get note ID from response")
    print("Note: This feature requires xcall")
    print("Install: https://github.com/martinfinke/xcall/releases")

    result = create_note(
        title="Important Note",
        text="This note has been created and its ID is returned.",
        tags="important",
        return_id=True
    )

    if result:
        print(f"Note created")
        print(f"   ID: {result.get('identifier')}")
        print(f"   Title: {result.get('title')}")
    else:
        print("xcall not installed or not configured")
        print("Install xcall and try again")
    print()


def example_multiline_note():
    """Complex markdown note creation"""
    print("Example 5: Complex markdown note creation")

    markdown_content = """# Project Report

## Executive Summary
This is a comprehensive report on the project status.

## Key Metrics

| Metric | Value |
|--------|-------|
| Progress | 75% |
| Team Size | 5 |
| Budget Used | $50K |

## Sections

### Completed
1. Design phase
2. Architecture review
3. Database setup

### In Progress
1. Backend API development
2. Frontend implementation

### Blocked
1. Performance optimization (waiting for infrastructure upgrade)

## Next Steps
- [ ] Complete API endpoints
- [ ] Implement authentication
- [ ] Start frontend integration testing
- [ ] Prepare deployment plan

## Notes
- Team morale is high
- No critical issues at the moment
- Schedule is on track
"""

    create_note(
        title="Project Report - Jan 2024",
        text=markdown_content,
        tags="project,report,monthly"
    )
    print("Complex markdown note created\n")


def example_quick_note():
    """Quick note creation"""
    print("Example 6: Quick notes")

    quick_ideas = [
        {"title": "Idea #1: Mobile App", "text": "Consider building native iOS app for better performance"},
        {"title": "Idea #2: Analytics", "text": "Implement real-time analytics dashboard"},
        {"title": "Idea #3: Automation", "text": "Automate deployment pipeline"}
    ]

    for idea in quick_ideas:
        create_note(
            title=idea["title"],
            text=idea["text"],
            tags="ideas,brainstorm"
        )
        print(f"  '{idea['title']}' created")

    print(f"Total {len(quick_ideas)} idea notes created\n")


if __name__ == "__main__":
    print("Bear Skill - Note Creation Examples\n")
    print("=" * 50)
    print()

    example_basic_note()
    example_note_with_tags()
    example_note_with_timestamp()
    example_note_with_response()
    example_multiline_note()
    example_quick_note()

    print("=" * 50)
    print("All examples completed!")
    print("\nTip: Check Bear app to see the created notes")
