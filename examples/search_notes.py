#!/usr/bin/env python3
"""
Bear Skill Example: Note Search

Demonstrates various ways to search notes.
"""

import sys
sys.path.insert(0, '../scripts')
from bear import search_notes
import os


def check_requirements():
    """Check prerequisites"""
    if not os.environ.get("BEAR_API_TOKEN"):
        print("Error: BEAR_API_TOKEN not set")
        print("\nSetup:")
        print("1. Bear app > Help > Advanced > API Token > Copy Token")
        print("2. export BEAR_API_TOKEN='your-token-here'")
        print("3. python3 search_notes.py")
        print("\nOr in one line:")
        print("BEAR_API_TOKEN='your-token' python3 search_notes.py")
        return False
    return True


def example_simple_search():
    """Simple search"""
    print("Example 1: Keyword search")
    print("Search term: 'python'")

    results = search_notes(term="python")

    if results:
        print(f"Found {len(results)} results\n")
        for i, note in enumerate(results[:5], 1):
            print(f"  {i}. {note.get('title', 'Untitled')}")
            print(f"     ID: {note.get('identifier')}")
    else:
        print("No search results\n")


def example_tag_filter_search():
    """Search with tag filter"""
    print("Example 2: Search with tag filter")
    print("Search: all notes, Tag filter: 'work'")

    results = search_notes(term="", tag="work")

    if results:
        print(f"Found {len(results)} notes with 'work' tag\n")
        for i, note in enumerate(results[:5], 1):
            print(f"  {i}. {note.get('title', 'Untitled')}")
            print(f"     Modified: {note.get('modificationDate', 'N/A')}")
    else:
        print("No notes with 'work' tag\n")


def example_search_with_term_and_tag():
    """Search with term and tag"""
    print("Example 3: Search term + tag filter")
    print("Search term: 'bug', Tag: 'development'")

    results = search_notes(term="bug", tag="development")

    if results:
        print(f"Found {len(results)} results\n")
        for i, note in enumerate(results[:5], 1):
            created = note.get('creationDate', 'N/A')
            print(f"  {i}. {note.get('title', 'Untitled')}")
            print(f"     Created: {created}")
    else:
        print("No search results\n")


def example_search_analysis():
    """Search all notes for analysis"""
    print("Example 4: Search all notes for analysis")
    print("Searching all notes...")

    results = search_notes(term="")

    if results:
        total_notes = len(results)
        print(f"Found {total_notes} total notes\n")

        # Recent 5 notes
        print("Recently modified notes (5):")
        recent = sorted(
            results,
            key=lambda x: x.get('modificationDate', ''),
            reverse=True
        )[:5]

        for i, note in enumerate(recent, 1):
            print(f"  {i}. {note.get('title', 'Untitled')}")
            print(f"     Modified: {note.get('modificationDate', 'N/A')}")

        print()

        # Oldest note
        oldest = min(results, key=lambda x: x.get('creationDate', ''))
        print(f"Oldest note:")
        print(f"  Title: {oldest.get('title', 'Untitled')}")
        print(f"  Created: {oldest.get('creationDate', 'N/A')}\n")
    else:
        print("No notes to search\n")


def example_search_with_filtering():
    """Filter search results"""
    print("Example 5: Filter search results")
    print("Search all notes, extract only those containing 'project'")

    results = search_notes(term="")

    if results:
        # Notes with 'project' in title
        filtered = [
            note for note in results
            if 'project' in note.get('title', '').lower()
        ]

        if filtered:
            print(f"Found {len(filtered)} project-related notes\n")
            for i, note in enumerate(filtered[:5], 1):
                print(f"  {i}. {note.get('title', 'Untitled')}")
        else:
            print("No project-related notes\n")
    else:
        print("No notes found\n")


def example_search_statistics():
    """Calculate note statistics"""
    print("Example 6: Note statistics")
    print("Searching all notes for statistics...")

    results = search_notes(term="")

    if results:
        print(f"Analysis complete\n")

        # Statistics
        total = len(results)
        print(f"Statistics:")
        print(f"  - Total notes: {total}")

        # Most recent note
        most_recent = max(
            results,
            key=lambda x: x.get('modificationDate', ''),
            default=None
        )
        if most_recent:
            print(f"  - Most recently modified: {most_recent.get('title', 'Untitled')}")
            print(f"    (Modified: {most_recent.get('modificationDate', 'N/A')})")

        print()

        # Sample notes
        print("Sample notes:")
        for note in results[:3]:
            title = note.get('title', 'Untitled')
            note_id = note.get('identifier', 'N/A')
            print(f"  - {title[:30]}... (ID: {note_id[:8]}...)")
    else:
        print("No notes to search\n")


if __name__ == "__main__":
    print("Bear Skill - Note Search Examples\n")
    print("=" * 50)
    print()

    # Check prerequisites
    if not check_requirements():
        exit(1)

    print()
    example_simple_search()
    example_tag_filter_search()
    example_search_with_term_and_tag()
    example_search_analysis()
    example_search_with_filtering()
    example_search_statistics()

    print("=" * 50)
    print("All search examples completed!")
    print("\nTips:")
    print("- Make sure BEAR_API_TOKEN is set")
    print("- xcall must be installed in /Applications to receive responses")
