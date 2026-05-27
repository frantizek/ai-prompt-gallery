# AI Prompt Gallery

A curated gallery of reusable AI prompt packs for image generation, creative work, and visual experimentation.

This repository is built around **prompt packs**: structured, copy-ready prompts designed to be easy to use, easy to modify, and capable of producing distinctive results with minimal effort.

---

## What This Repository Is

This is a public collection of prompts that are:

- worth trying
- easy to reuse
- visually or creatively distinctive
- structured for consistency
- useful for experimentation and iteration

The goal is not just to collect prompts, but to organize them into a reusable system that can scale over time.

---

## What Makes a Prompt Pack

Each prompt pack lives in its own folder and usually includes:

- `prompt.md` — the main copy-paste prompt
- `README.md` — explanation, usage, and metadata
- `examples.md` — simple substitutions or variations
- `gallery.md` — generated examples with captions
- `images/` — rendered samples

This structure keeps prompt text separate from explanation and showcase content.

---

## Prompt Design Principles

Most prompt packs in this repo follow a few core rules:

- **one main variable** whenever possible
- **strong visual or creative identity**
- **minimal setup**
- **high reuse value**
- **clear internal structure**

For example, many prompts are designed so you only need to replace something like:

`[CITY NAME]`

and generate immediately.

---

## Available Prompts

### 🏙️ Places & Travel

| Prompt | Description | Type | Status |
|--------|-------------|------|--------|
| [CityLine Poster](./prompts/cityline-poster/README.md) | Minimalist line-art city travel posters with editorial urban styling | City-name-only | Active |
| [Vintage Watercolor Poster](./prompts/vintage-watercolor-poster/README.md) | Hand-painted vacation-style city posters with nostalgic warmth | City-name-only | Active |
| [Cinematic Night Poster](./prompts/cinematic-night-poster/README.md) | Cinematic night city travel posters with glowing streets and moody urban atmosphere | City-name-only | Active |

### 👤 Faces & Portraits

| Prompt | Description | Type | Status |
|--------|-------------|------|--------|
| [Fantasy Tribal Portrait](./prompts/fantasy-tribal-portrait/) | Ultra-realistic cinematic fantasy portrait with tribal aesthetics | Subject-only | Active |
| [Fantasy Frost Warrior Portrait](./prompts/fantasy-frost-warrior-portrait/) | Ultra-realistic dark fantasy portrait with Nordic frost warrior theme | Subject-only | Active |
| [Cinematic Mini-Me Portrait](./prompts/cinematic-mini-me-portrait/) | Side-by-side portrait with cartoon-style miniature version | Subject-only | Active |

See the full prompt index in [prompts/README.md](./prompts/README.md).

---

## Quick Start

1. Open any prompt folder inside `prompts/`
2. Read the prompt pack `README.md`
3. Copy the contents of `prompt.md`
4. Replace the main variable, such as `[CITY NAME]`
5. Paste into your image generator
6. Generate and iterate if needed

Compatible with tools like **ChatGPT**, **DALL·E**, **Midjourney**, **Copilot**, **Stable Diffusion**, **SDXL**, **Flux**, and similar image models.

---

## Repository Structure

```text
prompts/
└── prompt-name/
    ├── README.md
    ├── prompt.md
    ├── examples.md
    ├── gallery.md
    └── images/
```

---

## Contributing

Want to add a new prompt pack, improve an existing one, or contribute sample outputs?

See [CONTRIBUTING.md](./CONTRIBUTING.md).