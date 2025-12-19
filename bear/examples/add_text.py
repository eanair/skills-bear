#!/usr/bin/env python3
"""
Bear Skill Example: Adding Text to Notes

Demonstrates various ways to add text to existing notes.
"""

import sys
sys.path.insert(0, '../scripts')
from bear import create_note, add_text, search_notes


def example_append_text():
    """Append text (append mode)"""
    print("Example 1: Append text to end of note")

    # Create test note first
    result = create_note(
        title="Meeting Notes",
        text="""# Meeting - January 15

## Attendees
- Alice
- Bob
- Charlie

## Agenda
- [ ] Project status
- [ ] Budget review
"""
    )

    print("Test note created")
    print("   Adding text...\n")

    # Add text to note by title
    add_text(
        note_title="Meeting Notes",
        text="""

## Action Items
- [ ] Alice: Prepare Q1 report (due Jan 20)
- [ ] Bob: Review budget estimates (due Jan 18)
- [ ] Charlie: Schedule follow-up meeting (due Jan 17)

## Notes
- Meeting was productive
- All team members present
""",
        mode="append"
    )

    print("Text appended")
    print("   Check Bear app\n")


def example_prepend_text():
    """Prepend text (prepend mode)"""
    print("Example 2: Add text to beginning of note")

    # Create test note
    create_note(
        title="Code Review",
        text="""## File: main.py
- Line 42: Needs error handling
- Line 89: Add type hints
"""
    )

    print("Test note created")
    print("   Adding text to beginning...\n")

    # Prepend
    add_text(
        note_title="Code Review",
        text="""# Code Review Log

Date: 2024-01-15
Reviewer: Alice

""",
        mode="prepend"
    )

    print("Text prepended\n")


def example_replace_all():
    """Replace entire note content"""
    print("Example 3: Replace entire note content")

    # Create test note
    create_note(
        title="TODO List",
        text="Old content that will be replaced"
    )

    print("Test note created (original: 'Old content...')")
    print("   Replacing entire content...\n")

    # Replace all
    add_text(
        note_title="TODO List",
        text="""# My TODO List

## High Priority
- [ ] Fix critical bug
- [ ] Update documentation
- [ ] Review pull requests

## Medium Priority
- [ ] Refactor code
- [ ] Add unit tests
- [ ] Optimize performance

## Low Priority
- [ ] Update comments
- [ ] Clean up old files
""",
        mode="replace_all"
    )

    print("Entire content replaced\n")


def example_append_to_header():
    """Add text only to specific header section"""
    print("Example 4: Add text to specific header section")

    # Create test note
    create_note(
        title="Project Plan",
        text="""# Project X Plan

## Timeline
- Week 1-2: Design phase

## Team
- Lead: Alice

## Budget
$100K allocated
"""
    )

    print("Test note created")
    print("   Adding text to 'Timeline' header...\n")

    # Add only to Timeline section
    add_text(
        note_title="Project Plan",
        text="\n- Week 3-4: Development phase",
        mode="append",
        header="Timeline"
    )

    print("Text added to 'Timeline' section\n")


def example_replace_first_occurrence():
    """Replace only first occurrence"""
    print("Example 5: Replace only first occurrence")

    # Create test note
    create_note(
        title="Inventory",
        text="""# Inventory

- Status: Out of stock
- Status: Out of stock
- Status: Out of stock
"""
    )

    print("Test note created")
    print("   Replacing first 'Out of stock' with 'In stock'...\n")

    # Replace first match only
    add_text(
        note_title="Inventory",
        text="In stock",
        mode="replace"
    )

    print("First occurrence replaced\n")


def example_update_status():
    """Update status"""
    print("Example 6: Update progress")

    # Create test note
    result = create_note(
        title="Q1 Progress",
        text="""# Q1 2024 Progress

## Week 1
- [ ] Task A
- [ ] Task B

## Week 2
- [ ] Task C
- [ ] Task D
""",
        tags="progress,quarterly"
    )

    print("Project progress note created")
    print("   Adding weekly progress...\n")

    # Add weekly progress
    update_text = """

## Week 3 (Current)
- [x] Task E
- [x] Task F
- [ ] Task G (blocked)
- [ ] Task H

### Notes
- Good progress despite one blocker
- Team working overtime
- Expect unblock by Friday
"""

    add_text(
        note_title="Q1 Progress",
        text=update_text,
        mode="append"
    )

    print("Weekly progress updated\n")


if __name__ == "__main__":
    print("Bear Skill - Text Addition Examples\n")
    print("=" * 50)
    print()

    example_append_text()
    example_prepend_text()
    example_replace_all()
    example_append_to_header()
    example_replace_first_occurrence()
    example_update_status()

    print("=" * 50)
    print("All text addition examples completed!")
    print("\nTips:")
    print("- Must specify either note_id or note_title")
    print("- mode options: append, prepend, replace_all, replace")
    print("- Specifying header applies changes only to that section")
    print("- Check Bear app to verify changes")
