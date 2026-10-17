# CodeAlpha_EmailExtractor

A Python automation script that finds all email addresses in a text file and saves them to a new file. Built as **Task 3 (Task Automation)** of the CodeAlpha Python Programming Internship.

## What it does

Imagine you have a long document full of text and you need to collect every email address from it. Doing that by hand is slow and boring. This script does it in a second:

1. Reads the text file `input.txt`
2. Finds every email address in it
3. Removes duplicates and sorts them
4. Saves the result to `emails_found.txt`

## Files in this project

| File | Purpose |
|------|---------|
| `email_extractor.py` | The script that does the work |
| `input.txt` | A sample text file containing some email addresses |
| `emails_found.txt` | Created automatically when you run the script |

## How to run

1. Install Python 3 from [python.org](https://www.python.org/downloads/) if you don't have it.
2. Download `email_extractor.py` and `input.txt` into the same folder.
3. Open a terminal in that folder and run:

```
python email_extractor.py
```

4. Open `emails_found.txt` to see the results.

To use your own text, replace the contents of `input.txt` with anything you like and run the script again.

## Example output

```
Found 4 unique email address(es).
  - john_doe99@example.com
  - priya.sharma@college.edu.in
  - services.codealpha@gmail.com
  - services@codealpha.tech

Saved to 'emails_found.txt'.
```

## Concepts used

`re` (regular expressions, used to describe what an email looks like), file reading and writing, sets (to remove duplicates), and error handling for a missing file.

## Author

Made by Yasin as part of the CodeAlpha Python Programming Internship.
