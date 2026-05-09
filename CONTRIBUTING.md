# Contributing a Prompt

## Structure

```
prompts/
└── your-prompt-name/
    ├── prompt.md           # The actual prompt
    ├── README.md           # Description + how to use + metadata
    ├── examples.md         # (Optional) Tips & variations
    ├── gallery.md          # (Optional) Generated images
    └── images/             # (Optional) Screenshots
        └── .gitkeep
```

## Required Metadata

Add at the top of your `README.md`:

```markdown
| | |
|---|---|
| **Generator** | e.g., ChatGPT, Claude, Midjourney, DALL-E, Copilot |
| **Version** | Prompt version |
| **Status** | Active / Archived |
```

## Gallery

For each image in gallery.md, add:

```markdown
**Generated with:** Microsoft Copilot
```

## Steps

1. Create a folder under `prompts/`
2. Add at minimum: `prompt.md` and `README.md` (with metadata)
3. (Optional) Add gallery, examples, and images
4. Update the main `README.md` table
5. Submit a PR

## Naming

- Lowercase with hyphens: `stylized-portrait`, `travel-poster`
- Short and descriptive
- Reflects the output type