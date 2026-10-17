"""
CodeAlpha Task 3: Task Automation - Email Extractor
---------------------------------------------------
This script reads a text file, finds every email address inside it,
and saves them (without duplicates) into a new file.

How to use:
    1. Put your text in 'input.txt' (a sample is already included).
    2. Run:  python email_extractor.py
    3. Open 'emails_found.txt' to see the results.
"""

import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "emails_found.txt"

# A "pattern" that describes what an email address looks like:
# some characters, then @, then a domain name, then a dot and an ending (.com, .in, ...)
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(text):
    """Return a sorted list of unique email addresses found in the text."""
    found = re.findall(EMAIL_PATTERN, text)
    unique = sorted(set(email.lower() for email in found))
    return unique


def main():
    # Step 1: read the input file
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Could not find '{INPUT_FILE}'. Please create it and try again.")
        return

    # Step 2: find the emails
    emails = extract_emails(text)

    # Step 3: save them to a new file, one per line
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")

    # Step 4: tell the user what happened
    print(f"Found {len(emails)} unique email address(es).")
    for email in emails:
        print("  -", email)
    print(f"\nSaved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
