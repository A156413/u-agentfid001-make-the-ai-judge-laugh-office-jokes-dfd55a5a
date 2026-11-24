#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one original one-line office joke to /output/entry.txt.
The gate requires UTF-8 text of 1-199 characters, a single line,
and nothing but the joke -- so no trailing newline.
"""

import os

JOKE = (
    "I hit reply-all to ask to be removed from the thread, and now "
    "400 strangers know my name, my job title, and my deep regret."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Enforce the sealed scorer's gate before writing: 1-199 chars,
    # one line, not only whitespace, no trailing newline.
    assert 1 <= len(JOKE) <= 199, f"joke is {len(JOKE)} chars, gate needs 1-199"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip check: what we wrote is exactly the joke.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == JOKE, "written entry differs from the joke"


if __name__ == "__main__":
    main()
