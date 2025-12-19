# Bear X-Callback-URL API Reference

Complete documentation for all X-Callback-URL actions supported by Bear app.

## Base Format

```
bear://x-callback-url/[action]?[parameters]&x-callback-parameters
```

## Contents

1. [Note Management](#note-management)
2. [Tag Management](#tag-management)
3. [Special Queries](#special-queries)
4. [Parameter Guide](#parameter-guide)

---

## Note Management

### /open-note - Open Note

Opens a specific note by ID or title and returns content.

**Required Parameters:**
- `id` or `title`: Note identifier

**Optional Parameters:**
- `header`: Jump to specific header in note
- `exclude_trashed`: Exclude trashed notes
- `new_window`: Open in external window (macOS)
- `edit`: Place cursor in editor
- `search`: Open find & replace panel

**Return Value:**
```json
{
  "note": "Full note text",
  "identifier": "7E4B681B",
  "title": "Note title",
  "tags": ["tag1", "tag2"],
  "modificationDate": "2024-01-15T10:30:00Z",
  "creationDate": "2024-01-01T09:00:00Z"
}
```

**Examples:**
```
bear://x-callback-url/open-note?id=7E4B681B&header=Secondary%20Title
bear://x-callback-url/open-note?title=My%20Note
```

---

### /create - Create New Note

Creates a new note and returns unique ID.

**Optional Parameters:**
- `title`: Note title
- `text`: Note content (Markdown supported)
- `clipboard`: Set `yes` to use clipboard content
- `tags`: Comma-separated tag list
- `file` + `filename`: base64 encoded file attachment
- `timestamp`: Set `yes` to add current date/time
- `type`: Set `html` for automatic HTML to Markdown conversion

**Return Value:**
```json
{
  "identifier": "7E4B681B",
  "title": "Created note title"
}
```

**Examples:**
```
bear://x-callback-url/create?title=My%20Note&text=First%20line&tags=home
bear://x-callback-url/create?title=Daily%20Log&text=Content&timestamp=yes
```

---

### /add-text - Add Text

Adds or modifies text in existing note.

**Required Parameters:**
- `id` or `title`: Target note
- `text`: Text to add

**Optional Parameters:**
- `mode`: Mode selection
  - `append`: Add to end (default)
  - `prepend`: Add to beginning
  - `replace_all`: Replace entire content
  - `replace`: Replace first match only
- `new_line`: Force new line in `append` mode
- `header`: Add only to specific header

**Return Value:**
```json
{
  "note": "Updated full text",
  "title": "Note title"
}
```

**Examples:**
```
bear://x-callback-url/add-text?id=4EDAF0D1&text=new%20line&mode=append
bear://x-callback-url/add-text?title=Project%20Notes&text=Update&mode=append&header=TODO
```

---

### /add-file - Add File

Attaches file to existing note.

**Required Parameters:**
- `file`: base64 encoded file data
- `filename`: Filename with extension

**Optional Parameters:**
- `id` or `title`: Target note (creates new note if not specified)
- `mode`: `append`, `prepend`, `replace_all`, `replace`
- `header`: Add only to specific header

**Return Value:**
```json
{
  "note": "Updated note text"
}
```

---

### /trash - Move to Trash

Moves note to trash.

**Parameters:**
- `id`: Note ID
- `search`: Search term (ignored if ID provided)

**Examples:**
```
bear://x-callback-url/trash?id=7E4B681B
bear://x-callback-url/trash?search=old%20note
```

---

### /archive - Move to Archive

Moves note to archive.

**Parameters:**
- `id`: Note ID
- `search`: Search term (ignored if ID provided)

**Examples:**
```
bear://x-callback-url/archive?id=7E4B681B
bear://x-callback-url/archive?search=completed
```

---

### /grab-url - Capture URL Content

Creates new note from web page content.

**Required Parameters:**
- `url`: URL to capture

**Optional Parameters:**
- `tags`: Tag list
- `pin`: Set `yes` to pin to top of list
- `wait`: Set `no` to call x-success before processing completes

**Return Value:**
```json
{
  "identifier": "7E4B681B",
  "title": "Captured page title"
}
```

**Examples:**
```
bear://x-callback-url/grab-url?url=https://bear.app
bear://x-callback-url/grab-url?url=https://example.com&tags=reference,web
```

---

## Tag Management

### /tags - Get All Tags

Returns all tags from sidebar.

**Required Parameters:**
- `token`: API token

**Return Value:**
```json
[
  { "name": "tag1" },
  { "name": "tag2" },
  { "name": "project/subtag" }
]
```

**Example:**
```
bear://x-callback-url/tags?token=123456-123456-123456
```

---

### /open-tag - Show Notes by Tag

Shows all notes with specific tag.

**Parameters:**
- `name`: Tag name (multiple allowed with comma)
- `token`: (Optional) Required for response

**Return Value:**
```json
[
  {
    "title": "Note title",
    "identifier": "7E4B681B",
    "modificationDate": "2024-01-15T10:30:00Z",
    "creationDate": "2024-01-01T09:00:00Z",
    "pin": false
  }
]
```

**Examples:**
```
bear://x-callback-url/open-tag?name=work
bear://x-callback-url/open-tag?name=project/task&token=TOKEN
```

---

### /rename-tag - Rename Tag

Renames existing tag.

**Required Parameters:**
- `name`: Current tag name
- `new_name`: New tag name

**Examples:**
```
bear://x-callback-url/rename-tag?name=todo&new_name=inbox
bear://x-callback-url/rename-tag?name=project/old&new_name=project/new
```

---

### /delete-tag - Delete Tag

Permanently deletes tag.

**Required Parameters:**
- `name`: Tag name

**Examples:**
```
bear://x-callback-url/delete-tag?name=archive
bear://x-callback-url/delete-tag?name=project/deprecated
```

---

## Special Queries

### /search - Search Notes

Searches notes by keyword.

**Parameters:**
- `term`: Search term (optional)
- `tag`: Search within specific tag only (optional)
- `token`: Required for return value

**Return Value:**
```json
[
  {
    "title": "Search result note",
    "identifier": "7E4B681B",
    "modificationDate": "2024-01-15T10:30:00Z",
    "creationDate": "2024-01-01T09:00:00Z"
  }
]
```

**Examples:**
```
bear://x-callback-url/search?term=Python&token=TOKEN
bear://x-callback-url/search?term=bug&tag=development&token=TOKEN
```

---

### /todo - Todo Items

Shows notes with todo status.

**Parameters:**
- `search`: Search term (optional)
- `token`: Required for return value

**Examples:**
```
bear://x-callback-url/todo?token=TOKEN
bear://x-callback-url/todo?search=urgent&token=TOKEN
```

---

### /today - Today Items

Shows notes created/modified today.

**Parameters:**
- `search`: Search term (optional)
- `token`: Required for return value

**Examples:**
```
bear://x-callback-url/today?token=TOKEN
bear://x-callback-url/today?search=standup&token=TOKEN
```

---

### /untagged - Untagged Items

Shows notes without tags.

**Parameters:**
- `search`: Search term (optional)
- `token`: Required for return value

**Example:**
```
bear://x-callback-url/untagged?token=TOKEN
```

---

### /locked - Locked Items

Shows password-locked notes.

**Parameters:**
- `search`: Search term (optional)

**Example:**
```
bear://x-callback-url/locked?search=sensitive
```

---

## Parameter Guide

### Encoding

Spaces and special characters in URLs must be encoded:

```
"Hello World" -> "Hello%20World"
"Project/2024" -> "Project%2F2024"
```

Encoding in Python:

```python
import urllib.parse
encoded = urllib.parse.quote("Hello World")
# -> "Hello%20World"
```

### Token

Following actions require API token for response:

- `/tags`
- `/search`
- `/open-tag` (with response)
- `/todo` (with response)
- `/today` (with response)
- `/untagged` (with response)

Get token from macOS Bear:
1. Help > Advanced > API Token
2. Copy Token
3. Set environment variable: `export BEAR_API_TOKEN="token"`

**Important:** iOS token and macOS token are not compatible.

### Response Handling

Use xcall tool when response is needed:

```bash
# Install xcall
# https://github.com/martinfinke/xcall/releases -> /Applications/xcall.app

# Get response
/Applications/xcall.app/Contents/MacOS/xcall -url "bear://x-callback-url/search?term=python&token=TOKEN"
```

Simple execution without response:

```bash
# Use open command
open "bear://x-callback-url/open-tag?name=work"
```
