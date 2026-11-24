"""The One-Line Cat Joke That Lands - entry program.

Writes a single joke about cats, one line under 200 characters,
to /output/entry.txt. The entry holds exactly the joke line.
"""

import os

JOKE = "My cat has never paid rent, never done a dish, and still takes the sunny spot on the bed — so now I just call him my landlord."


def main():
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
