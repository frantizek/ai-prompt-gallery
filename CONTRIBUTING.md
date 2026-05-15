# Contributing

Thanks for contributing to AI Prompt Gallery.

This repository is organized around **prompt packs**: reusable prompt folders with a consistent internal structure so prompts are easy to browse, copy, test, and expand.

---

## Prompt Pack Structure

Create a folder under `prompts/` using a short, descriptive, hyphenated name.

```text
prompts/
└── your-prompt-name/
    ├── README.md
    ├── prompt.md
    ├── examples.md
    ├── gallery.md
    └── images/
        └── .gitkeep
```

### Required files

- `README.md`
- `prompt.md`

### Strongly recommended files

- `examples.md`
- `gallery.md`
- `images/`

---

## File Roles

### `README.md`
Use this file to explain:

- what the prompt does
- why it works
- best use cases
- how to use it
- what the main variable is
- which models it works well with

### `prompt.md`
Use this file for the **main prompt only**.

Keep it clean and copy-ready:
- no long explanations
- no gallery notes
- no metadata blocks
- no usage guide text

### `examples.md`
Use this file for simple substitutions, filled-in examples, or small prompt variations.

### `gallery.md`
Use this file to showcase outputs generated with the prompt.

### `images/`
Store sample outputs here.

---

## README Metadata Format

At the top of each prompt pack `README.md`, include these sections:

```md
## Prompt Type
[Example: City-name-only master prompt]

## Difficulty
[Example: Easy]

## Variables
[Example: 1 — `[CITY NAME]`]

## Best Models
[Example: Midjourney, DALL·E, ChatGPT, SDXL, Flux]

## Output Style
[Example: Travel poster / destination branding / collectible print]
```

---

## Prompt Design Guidelines

Prompt packs in this repository should aim to be:

- easy to reuse
- easy to modify
- high impact
- clearly structured
- visually or creatively distinctive

Whenever possible:

- use **one main variable**
- keep the prompt focused on one strong output type
- avoid unnecessary parameter overload
- make the prompt usable with minimal editing

Good prompt packs often let the user change only one thing, such as:

`[CITY NAME]`

---

## Preferred Prompt Structure

For image prompts, this sequence works well:

1. concept sentence
2. scene description
3. title or text instruction if relevant
4. style block
5. composition block
6. output block

---

## Naming Rules

Use folder names that are:

- lowercase
- hyphen-separated
- short
- descriptive

### Good examples

- `cityline-poster`
- `vintage-watercolor-poster`
- `cinematic-night-poster`
- `retro-futurist-poster`

### Avoid

- `PromptV2`
- `my_prompt`
- `test-folder`
- overly long names

---

## Gallery Notes

In `gallery.md`, include generator attribution when known.

Example:

```md
**Generated with:** ChatGPT
```

Optional additions:
- short notes
- color palette
- comparison comments

Keep gallery entries concise.

---

## Adding a New Prompt Pack

1. Create a folder under `prompts/`
2. Add at minimum:
   - `README.md`
   - `prompt.md`
3. Add `examples.md`, `gallery.md`, and `images/` when possible
4. Add your prompt pack to:
   - root `README.md`
   - `prompts/README.md`
5. Submit your changes

---

## Quality Checklist

Before contributing, ask:

- Is the prompt easy to understand?
- Is it easy to copy and reuse?
- Does it produce a distinct result?
- Does it fit the prompt-pack structure?
- Is the folder name clear and descriptive?

If yes, it likely fits the repository well.