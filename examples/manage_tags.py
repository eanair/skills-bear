#!/usr/bin/env python3
"""
Bear Skill Example: Tag Management

Demonstrates how to list, rename, and delete tags.
"""

import sys
sys.path.insert(0, '../scripts')
from bear import get_tags, rename_tag, delete_tag, open_tag, create_note
import os


def check_requirements():
    """Check prerequisites"""
    if not os.environ.get("BEAR_API_TOKEN"):
        print("Error: BEAR_API_TOKEN not set")
        print("\nSetup:")
        print("1. Bear app > Help > Advanced > API Token > Copy Token")
        print("2. export BEAR_API_TOKEN='your-token-here'")
        print("3. python3 manage_tags.py")
        return False
    return True


def example_list_all_tags():
    """List all tags"""
    print("Example 1: List all tags")

    tags = get_tags()

    if tags:
        print(f"Found {len(tags)} tags\n")
        print("Tag list:")
        for i, tag in enumerate(tags[:10], 1):
            print(f"  {i}. {tag['name']}")
        if len(tags) > 10:
            print(f"  ... and {len(tags) - 10} more")
    else:
        print("No tags to list\n")


def example_organize_tags():
    """Analyze tag structure"""
    print("Example 2: Analyze tag structure")

    tags = get_tags()

    if tags:
        # Classify top-level tags and subtags
        top_level = {}
        for tag in tags:
            name = tag['name']
            if '/' in name:
                parent = name.split('/')[0]
                if parent not in top_level:
                    top_level[parent] = []
                top_level[parent].append(name)
            else:
                if 'root' not in top_level:
                    top_level['root'] = []
                top_level['root'].append(name)

        print(f"Tag structure analyzed\n")
        print("Hierarchy:")
        for parent, children in sorted(top_level.items()):
            if parent == 'root':
                print(f"\nTop-level tags ({len(children)}):")
                for child in children[:5]:
                    print(f"  - {child}")
                if len(children) > 5:
                    print(f"  ... and {len(children) - 5} more")
            else:
                print(f"\n{parent}/ ({len(children)}):")
                for child in children[:3]:
                    print(f"  - {child}")
                if len(children) > 3:
                    print(f"  ... and {len(children) - 3} more")
    else:
        print("No tags\n")


def example_open_tag_view():
    """Open specific tag view"""
    print("Example 3: Open specific tag view")
    print("Opening 'work' tag view")
    print("(Check Bear app to see notes with 'work' tag)\n")

    open_tag("work")

    print("'work' tag view opened")
    print("   Check Bear app\n")


def example_create_and_organize():
    """Create notes and organize with tags"""
    print("Example 4: Create notes and organize with tags")

    # Create multiple notes with various tags
    notes_data = [
        {
            "title": "Project Alpha - Phase 1",
            "text": "Phase 1 of Project Alpha",
            "tags": "project,alpha,phase1"
        },
        {
            "title": "Project Alpha - Phase 2",
            "text": "Phase 2 of Project Alpha",
            "tags": "project,alpha,phase2"
        },
        {
            "title": "Development Setup",
            "text": "Development environment guide",
            "tags": "dev,setup,guide"
        },
    ]

    print("Creating the following notes:")
    for note in notes_data:
        print(f"  - {note['title']} (tags: {note['tags']})")
        create_note(
            title=note['title'],
            text=note['text'],
            tags=note['tags']
        )

    print("\nAll notes created and organized with tags\n")


def example_rename_tag_demonstration():
    """Tag rename demonstration (not actually executed)"""
    print("Example 5: Tag rename demonstration")
    print("Note: This example is not actually executed")
    print("   Modify the code to actually rename tags\n")

    print("Usage:")
    print("  rename_tag(old_name='old-tag', new_name='new-tag')\n")

    print("Example explanation complete")
    print("   Note: Renaming a tag affects all notes with that tag\n")


def example_tag_statistics():
    """Tag statistics"""
    print("Example 6: Tag statistics")

    tags = get_tags()

    if tags:
        total_tags = len(tags)
        has_subtags = sum(1 for t in tags if '/' in t['name'])

        print(f"Statistics calculated\n")
        print("Tag statistics:")
        print(f"  - Total tags: {total_tags}")
        print(f"  - Subtags: {has_subtags}")
        print(f"  - Top-level tags: {total_tags - has_subtags}")

        # Longest tag name
        longest = max(tags, key=lambda x: len(x['name']))
        print(f"\n  - Longest tag: {longest['name']} ({len(longest['name'])} chars)")

        # Shortest tag name
        shortest = min(tags, key=lambda x: len(x['name']))
        print(f"  - Shortest tag: {shortest['name']} ({len(shortest['name'])} chars)")
    else:
        print("No tags\n")


def example_tag_workflow():
    """Tag workflow example"""
    print("Example 7: Tag workflow")
    print("Project management scenario\n")

    workflow = """
1. Create project
   - Tags: project/alpha, active

2. Project progress
   - Add note: project/alpha/phase1
   - Add note: project/alpha/phase2

3. Project review
   - Use open_tag('project/alpha') to view all related notes

4. Project completion
   - Rename tag: project/alpha -> project/alpha-archived
   - Or add 'completed' tag

5. Tag cleanup
   - Delete unused tags
"""

    print(workflow)
    print("\nWorkflow explanation complete\n")


if __name__ == "__main__":
    print("Bear Skill - Tag Management Examples\n")
    print("=" * 50)
    print()

    # Check prerequisites
    if not check_requirements():
        exit(1)

    print()
    example_list_all_tags()
    example_organize_tags()
    example_open_tag_view()
    example_create_and_organize()
    example_rename_tag_demonstration()
    example_tag_statistics()
    example_tag_workflow()

    print("=" * 50)
    print("All tag management examples completed!")
    print("\nTips:")
    print("- Make sure BEAR_API_TOKEN is set")
    print("- Subtags are separated by '/' (e.g., project/alpha)")
    print("- Renaming and deleting tags affects all related notes")
    print("- Use open_tag() to view all notes with a specific tag")
