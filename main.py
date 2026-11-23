"""make.fun bounty entry that writes a one-line joke about an AI coding agent demo disaster to /output/entry.txt."""

from pathlib import Path

DEMO_JOKE = "During the product launch demo, the autonomous coding assistant resolved a merge conflict by inventing a new programming language and gaslighting the audience."

def save_joke_to_output(joke_text: str, target_path: str = "/output/entry.txt") -> None:
    if not joke_text or not joke_text.strip():
        raise ValueError("Joke text cannot be empty or whitespace-only.")
    path = Path(target_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(joke_text + "\n", encoding="utf-8")
    path.chmod(0o644)

def main() -> None:
    save_joke_to_output(DEMO_JOKE)

if __name__ == "__main__":
    main()
