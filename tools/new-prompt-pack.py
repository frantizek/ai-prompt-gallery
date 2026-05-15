#!/usr/bin/env python3

from pathlib import Path
import sys


def slug_to_title(slug: str) -> str:
    return " ".join(word.capitalize() for word in slug.split("-"))


def write_file(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python tools/new-prompt-pack.py <prompt-pack-name>")
        sys.exit(1)

    slug = sys.argv[1].strip()
    if not slug:
        print("Error: prompt-pack-name cannot be empty.")
        sys.exit(1)

    root = Path(__file__).resolve().parent.parent
    prompts_dir = root / "prompts"
    pack_dir = prompts_dir / slug
    images_dir = pack_dir / "images"

    if pack_dir.exists():
        print(f"Error: prompt pack '{slug}' already exists.")
        sys.exit(1)

    title = slug_to_title(slug)

    readme_content = f"""
# {title}

A reusable prompt pack for generating distinctive outputs with a consistent structure.

## Prompt Type
[Describe the prompt type]

## Difficulty
Easy

## Variables
1 — `[MAIN VARIABLE]`

## Best Models
ChatGPT, DALL·E, Midjourney, Copilot, SDXL, Flux

## Output Style
[Describe the output style]

## What It Does

Describe what this prompt generates and what makes the output visually or creatively distinctive.

## Why It Works

- strong visual or creative identity
- easy to reuse
- minimal setup
- clear structure
- suitable for iteration

## Best For

- [use case 1]
- [use case 2]
- [use case 3]

## How to Use

1. Open `prompt.md`
2. Copy the prompt
3. Replace the main variable
4. Paste into your preferred AI tool
5. Generate and iterate if needed

## Files

- `prompt.md` — main master prompt
- `examples.md` — example substitutions or variations
- `gallery.md` — sample outputs
- `images/` — rendered examples
"""

    prompt_content = """# Prompt

```text
[PASTE MAIN PROMPT HERE]
```
"""

    examples_content = """# Examples

These examples use the same prompt and change only the main variable.

## Example Replacements

- Example One
- Example Two
- Example Three

## Example Usage

Replace:

`[MAIN VARIABLE]`

With:

`Example One`
"""

    gallery_content = f"""# Gallery

This gallery is being prepared for the current {title} prompt pack.

Future examples in this folder should be generated using the current `prompt.md` so the showcase stays consistent with the public prompt pack.

## Planned Examples

- Example One
- Example Two
- Example Three

## Notes

Use `images/` to store new outputs and add short captions with generator attribution when available.
"""

    pack_dir.mkdir(parents=True, exist_ok=False)
    images_dir.mkdir(parents=True, exist_ok=False)

    write_file(pack_dir / "README.md", readme_content)
    write_file(pack_dir / "prompt.md", prompt_content)
    write_file(pack_dir / "examples.md", examples_content)
    write_file(pack_dir / "gallery.md", gallery_content)
    write_file(images_dir / ".gitkeep", "")

    print(f"Created prompt pack: {pack_dir.relative_to(root)}")


if __name__ == "__main__":
    main()