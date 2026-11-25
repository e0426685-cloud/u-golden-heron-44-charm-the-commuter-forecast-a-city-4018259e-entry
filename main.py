"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for a city
that does not exist, to /output/entry.txt.

Python standard library only.
"""

import os

ENTRY = (
    "Mizzleford this morning: grey skies and light drizzle, "
    "with a 100% chance the bus driver waits when he sees you running."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """Check the entry against the bounty brief's constraints."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1 to {MAX_CHARS} characters, got {len(text)}"
    )
    assert text.strip(), "entry must not be only white space"
    assert text == text.strip(), "entry must not have leading/trailing white space"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8 text
    assert "Mizzleford" in text, "entry must name the invented city"
    assert "drizzle" in text, "entry must give the city weather"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    # Verify the round trip: what landed on disk must be exactly the
    # validated entry, or the run has not produced a usable submission.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from validated entry"
    validate(written)
    print(f"entry written ({len(written)}/{MAX_CHARS} chars): {written}")


if __name__ == "__main__":
    main()
