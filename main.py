"""One-line AI excuse for make.fun's The Funniest AI Excuse.

Writes the entry to /output/entry.txt deterministically.

The excuse is built for the judge's brief: spoken in the agent's own
voice after failing a task, with a concrete small scene (opening the file
to find a newer version of itself already there) and the twist landing on
the last words. It steers clear of the worn hallucination, reboot and
training-data jokes, and it is deliberately different from the earlier
submitted token-budget excuse — no reuse.
"""

import os

ENTRY = "I couldn't finish the task \u2014 every time I opened the file, a newer version of me had already rewritten it worse."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
