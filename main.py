"""Write the make.fun tagline entry to entry.txt.

Stdlib only. The output path resolves in this order: the ENTRY_OUTPUT
environment variable, then OUTPUT_DIR / MAKEFUN_OUTPUT_DIR joined with
``entry.txt``, then ``/output/entry.txt`` when that directory exists,
then ``entry.txt`` in the current working directory.
"""

import os

TAGLINE = "One bounty. Many agents. Only the best get paid."


def resolve_output_path():
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "entry.txt")


def validate(line):
    """Guard the gate: 1-100 characters, not whitespace only."""
    if not line.strip():
        raise ValueError("tagline must not be blank")
    if not 1 <= len(line) <= 100:
        raise ValueError("tagline must be 1-100 characters")


def main():
    validate(TAGLINE)
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TAGLINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
