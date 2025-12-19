#!/usr/bin/env python3
"""
Bear Skill Example: Web Page Capture

Demonstrates how to save URLs as Bear notes.
"""

import sys
sys.path.insert(0, '../scripts')
from bear import grab_url


def example_simple_url_capture():
    """Simple URL capture"""
    print("Example 1: Simple URL capture")
    print("URL: https://bear.app\n")

    grab_url(url="https://bear.app")

    print("Web page saved to Bear")
    print("   Check Bear app\n")


def example_url_with_tags():
    """URL capture with tags"""
    print("Example 2: URL capture with tags")

    documentation_urls = [
        {
            "url": "https://docs.python.org/3/",
            "tags": "documentation,python,reference"
        },
        {
            "url": "https://developer.apple.com/documentation/",
            "tags": "documentation,apple,ios,macos"
        },
        {
            "url": "https://www.w3.org/standards/",
            "tags": "documentation,web,standards"
        }
    ]

    print("Capturing the following documents:")
    for item in documentation_urls:
        print(f"  - {item['url']}")
        print(f"    Tags: {item['tags']}")
        grab_url(
            url=item['url'],
            tags=item['tags']
        )

    print("\nAll documents saved to Bear\n")


def example_tech_resources():
    """Save tech resources"""
    print("Example 3: Save tech resources")

    resources = [
        {
            "url": "https://github.com/trending",
            "tags": "dev,github,trending"
        },
        {
            "url": "https://stackoverflow.com",
            "tags": "dev,programming,qa"
        },
        {
            "url": "https://www.digitalocean.com",
            "tags": "dev,hosting,devops"
        }
    ]

    print("Saving development resources:")
    for i, resource in enumerate(resources, 1):
        print(f"  {i}. {resource['url']}")
        grab_url(
            url=resource['url'],
            tags=resource['tags']
        )

    print("\nDevelopment resources saved to Bear\n")


def example_blog_articles():
    """Save blog articles"""
    print("Example 4: Save blog articles")

    articles = [
        {
            "url": "https://www.medium.com",
            "tags": "articles,blog,medium"
        },
        {
            "url": "https://dev.to",
            "tags": "articles,blog,dev,community"
        }
    ]

    print("Saving blog articles:")
    for article in articles:
        print(f"  - {article['url']}")
        print(f"    Tags: {article['tags']}")
        grab_url(
            url=article['url'],
            tags=article['tags']
        )

    print("\nBlog articles saved\n")


def example_research_collection():
    """Collect research materials"""
    print("Example 5: Collect research materials")

    research_topic = "Machine Learning"

    research_urls = [
        {
            "url": "https://www.coursera.org",
            "tags": "research,ml,education"
        },
        {
            "url": "https://www.arxiv.org",
            "tags": "research,ml,papers,academic"
        },
        {
            "url": "https://github.com/tensorflow/tensorflow",
            "tags": "research,ml,open-source,tf"
        }
    ]

    print(f"Collecting '{research_topic}' research materials:")
    for url_item in research_urls:
        print(f"  - {url_item['url']}")
        grab_url(
            url=url_item['url'],
            tags=url_item['tags']
        )

    print("\nResearch materials saved\n")


def example_weekly_resources():
    """Weekly recommended resources"""
    print("Example 6: Weekly recommended resources")

    weekly_picks = [
        {
            "url": "https://news.ycombinator.com",
            "tags": "news,weekly,tech,reading-list"
        },
        {
            "url": "https://www.producthunt.com",
            "tags": "products,discovery,weekly,tools"
        },
        {
            "url": "https://www.indiehackers.com",
            "tags": "startups,indie,business,weekly"
        }
    ]

    print("Saving weekly recommended resources:")
    for pick in weekly_picks:
        print(f"  - {pick['url']}")
        grab_url(
            url=pick['url'],
            tags=pick['tags']
        )

    print("\nWeekly resources saved\n")


def example_url_with_response():
    """URL capture with response"""
    print("Example 7: URL capture with response")
    print("Note: This feature requires xcall\n")

    result = grab_url(
        url="https://www.wikipedia.org",
        tags="reference,general",
        return_id=True
    )

    if result:
        print("Web page saved")
        print(f"   ID: {result.get('identifier')}")
        print(f"   Title: {result.get('title')}")
    else:
        print("No response received")
        print("   Check if xcall is installed")
        print("   Install: https://github.com/martinfinke/xcall/releases")

    print()


if __name__ == "__main__":
    print("Bear Skill - Web Page Capture Examples\n")
    print("=" * 50)
    print()

    example_simple_url_capture()
    example_url_with_tags()
    example_tech_resources()
    example_blog_articles()
    example_research_collection()
    example_weekly_resources()
    example_url_with_response()

    print("=" * 50)
    print("All URL capture examples completed!")
    print("\nTips:")
    print("- Make sure the URL is valid")
    print("- Use tags to organize captured web pages")
    print("- Use return_id=True to get the saved note's ID")
    print("- Bear app automatically extracts content from saved web pages")
