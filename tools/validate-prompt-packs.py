#!/usr/bin/env python3

from pathlib import Path
import sys


REQUIRED_ROOT_FILES = [
    "README.md",
    "CONTRIBUTING.md",
]

REQUIRED_PACK_FILES = [
    "README.md",
    "prompt.md",
    "examples.md",
    "gallery.md",
]

REQUIRED_METADATA_HEADINGS = [
    "## Prompt Type",
    "## Difficulty",
    "## Variables",
    "## Best Models",
    "## Output Style",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_root(root: Path) -> list[str]:
    errors = []

    for name in REQUIRED_ROOT_FILES:
        if not (root / name).exists():
            errors.append(f"Missing root file: {name}")

    prompts_dir = root / "prompts"
    if not prompts_dir.exists() or not prompts_dir.is_dir():
        errors.append("Missing prompts/ directory")
    else:
        if not (prompts_dir / "README.md").exists():
            errors.append("Missing prompts/README.md")

    return errors


def validate_pack(pack_dir: Path) -> list[str]:
    errors = []

    for name in REQUIRED_PACK_FILES:
        if not (pack_dir / name).exists():
            errors.append(f"{pack_dir.name}: missing {name}")

    images_dir = pack_dir / "images"
    if not images_dir.exists() or not images_dir.is_dir():
        errors.append(f"{pack_dir.name}: missing images/ directory")
    elif not any(images_dir.iterdir()):
        errors.append(f"{pack_dir.name}: images/ is empty (expected .gitkeep or sample images)")

    readme_path = pack_dir / "README.md"
    if readme_path.exists():
        readme = read_text(readme_path)
        for heading in REQUIRED_METADATA_HEADINGS:
            if heading not in readme:
                errors.append(f"{pack_dir.name}: README.md missing heading '{heading}'")

    prompt_path = pack_dir / "prompt.md"
    if prompt_path.exists():
        prompt = read_text(prompt_path)
        if "# Prompt" not in prompt:
            errors.append(f"{pack_dir.name}: prompt.md missing '# Prompt' heading")
        if "```text" not in prompt:
            errors.append(f"{pack_dir.name}: prompt.md missing text code block")

    return errors


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    errors = validate_root(root)

    prompts_dir = root / "prompts"
    if prompts_dir.exists():
        for child in sorted(prompts_dir.iterdir()):
            if child.is_dir():
                errors.extend(validate_pack(child))

    if errors:
        print("Validation failed:\n")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("Validation passed.")


if __name__ == "__main__":
    main()