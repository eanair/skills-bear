# Troubleshooting Guide

Common issues and solutions when using Bear Skill.

## Contents

1. [Setup Issues](#setup-issues)
2. [API Token Issues](#api-token-issues)
3. [xcall Issues](#xcall-issues)
4. [Note Operation Issues](#note-operation-issues)
5. [Search and Tag Issues](#search-and-tag-issues)

---

## Setup Issues

### Bear App Not Installed

**Symptom:** Bear doesn't open when running `open` command

**Solution:**
1. Verify Bear app is installed
2. Download from Mac App Store or [bear.app](https://bear.app)
3. Run at least once after installation to complete system registration

```bash
# Check Bear app location
ls -la /Applications/Bear.app
```

---

## API Token Issues

### Token Not Set

**Symptom:**
```
Search results: None
Tag query failed
```

**Cause:** Search, tags, and special query features require API token.

**Solution:**

1. **Get token from macOS Bear:**
   - Run Bear app
   - Top menu > Help
   - Advanced > API Token
   - Click Copy Token

2. **Set environment variable:**

   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   export BEAR_API_TOKEN="your-token-here"

   # Apply settings
   source ~/.zshrc

   # Verify
   echo $BEAR_API_TOKEN
   ```

3. **Verify in Python script:**

   ```python
   import os
   token = os.environ.get("BEAR_API_TOKEN")
   if token:
       print(f"Token set: {token[:10]}...")
   else:
       print("Token not set")
   ```

### iOS and macOS Tokens Not Compatible

**Symptom:** Token from iOS doesn't work on macOS

**Solution:**
- iOS and macOS use separate tokens
- Use macOS Bear token for macOS operations
- Use iOS Bear token for iOS operations

### Token Verification

```bash
# Verify token with xcall
/Applications/xcall.app/Contents/MacOS/xcall -url "bear://x-callback-url/tags?token=$BEAR_API_TOKEN"

# If response is JSON array, token is valid
# If error, verify token again
```

---

## xcall Issues

### xcall Not Installed

**Symptom:**
- Features requiring response don't work
- `return_id=True` option ignored

**Solution:**

1. **Download xcall:**
   - Go to [xcall GitHub Releases](https://github.com/martinfinke/xcall/releases)
   - Download latest `xcall.zip`

2. **Install:**

   ```bash
   # Extract downloaded file
   unzip ~/Downloads/xcall.zip

   # Move to Applications folder
   mv ~/Downloads/xcall.app /Applications/

   # Set permissions
   chmod +x /Applications/xcall.app/Contents/MacOS/xcall
   ```

3. **Verify installation:**

   ```bash
   /Applications/xcall.app/Contents/MacOS/xcall --help
   # Help displayed means setup complete
   ```

### xcall Path Incorrect

**Symptom:**
```
xcall: No such file or directory
```

**Solution:**

Check `XCALL_PATH` setting in Python script:

```python
# In bear.py
XCALL_PATH = "/Applications/xcall.app/Contents/MacOS/xcall"

# Override with environment variable if different path
import os
XCALL_PATH = os.environ.get("XCALL_PATH", "/Applications/xcall.app/Contents/MacOS/xcall")
```

### xcall Response Not JSON

**Symptom:**
```
json.JSONDecodeError: Expecting value
```

**Cause:** xcall returned error message or Bear app couldn't process response

**Solution:**

```bash
# Test xcall directly
/Applications/xcall.app/Contents/MacOS/xcall -url "bear://x-callback-url/create?title=Test&text=Content"

# Check response
echo $?  # 0 means success, non-zero means failure
```

---

## Note Operation Issues

### Note Creation Not Working

**Symptom:** Note not created in Bear after `create_note()` call

**Checklist:**

1. Verify Bear app is running
2. Verify title is not empty
3. Check permissions (Bear has file system access)

**Test code:**

```python
from scripts.bear import create_note

# Create simple test note
create_note(
    title="Test Note",
    text="This is a test",
    tags="test"
)

print("Note creation request complete")
print("Check Bear app")
```

### Special Characters Not Encoding Properly

**Symptom:** Korean or special characters appear broken

**Solution:** Python script handles URL encoding automatically.

```python
# This code handles encoding automatically
create_note(
    title="Korean Title",
    text="Korean content\nSpecial chars: @#$%"
)
```

For manual URL creation:

```python
import urllib.parse

title = "Korean Title"
encoded = urllib.parse.quote(title)
# -> URL encoded string

url = f"bear://x-callback-url/create?title={encoded}"
```

### Text Addition Not Working

**Symptom:** Note content unchanged after `add_text()`

**Checklist:**

1. **Verify note ID is correct:**

   ```python
   from scripts.bear import search_notes

   # Search for note to get ID
   results = search_notes(term="part of note title")
   if results:
       note_id = results[0]['identifier']
       print(f"Note ID: {note_id}")
   ```

2. **Check if note is encrypted:**
   - Cannot add text to encrypted notes
   - Decrypt note first then try again

3. **Verify mode is correct:**

   ```python
   # mode options: append, prepend, replace_all, replace
   add_text(
       note_id="YOUR_NOTE_ID",
       text="Text to add",
       mode="append"  # default
   )
   ```

---

## Search and Tag Issues

### No Search Results

**Symptom:**
```python
results = search_notes(term="python")
# Returns None or empty list
```

**Checklist:**

1. **Verify API token is set:**
   ```bash
   echo $BEAR_API_TOKEN
   ```

2. **Verify search term is correct:**
   - Bear supports full-text search
   - Case insensitive

3. **Verify note actually exists:**
   - Search directly in Bear app

4. **Verify xcall is installed:**
   ```bash
   ls -la /Applications/xcall.app
   ```

### Tag Query Fails

**Symptom:**
```python
tags = get_tags()
# Returns None
```

**Solution:**

```python
import os
from scripts.bear import get_tags

# 1. Check token
token = os.environ.get("BEAR_API_TOKEN")
if not token:
    print("Token not set")
    print("Set with: export BEAR_API_TOKEN='your-token'")
    exit(1)

# 2. Check xcall
import os as os2
if not os2.path.exists("/Applications/xcall.app/Contents/MacOS/xcall"):
    print("xcall not installed")
    exit(1)

# 3. Try tag query
tags = get_tags()
if tags:
    print(f"Found {len(tags)} tags")
    for tag in tags:
        print(f"  - {tag['name']}")
else:
    print("Tag query failed")
```

### Tag Filtering Not Working

**Symptom:**
```python
results = search_notes(term="python", tag="development")
# Fewer results than expected
```

**Solution:**

1. **Verify tag name is correct:**
   ```python
   from scripts.bear import get_tags

   tags = get_tags()
   tag_names = [tag['name'] for tag in tags]
   print("Available tags:", tag_names)
   ```

2. **Use subtags:**
   ```python
   # Hierarchical tags
   search_notes(term="", tag="project/work")
   ```

---

## Common Error Messages

### "BEAR_API_TOKEN not found"

**Solution:**
```bash
export BEAR_API_TOKEN="your-token-here"
```

### "Connection refused"

**Solution:**
1. Verify Bear app is running
2. Try restarting Mac

### "Invalid URL"

**Solution:**
- Python script handles encoding automatically
- Use `urllib.parse.quote()` for manual URL creation

---

## Debugging Tips

### Enable Detailed Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from scripts.bear import create_note

# Check call status via logging
create_note(
    title="Debug Test",
    text="Testing",
    tags="test"
)
```

### Check Bear App Status

```bash
# Check Bear process
ps aux | grep Bear

# Check Bear logs
log stream --predicate 'process == "Bear"'
```

### Verify Python Environment

```bash
python3 --version
python3 -c "import urllib.parse; print('urllib working')"
python3 -c "import subprocess; print('subprocess working')"
```

---

## Additional Support

For more help:

1. Bear official documentation: https://bear.app/faq/
2. X-Callback-URL spec: https://x-callback-url.com/
3. xcall project: https://github.com/martinfinke/xcall
