# Obsidian Quickstart For This Repository

This repository is structured as an Obsidian-first LLM learning vault, not just a Markdown folder.

## What Was Set Up

- `.obsidian/app.json` enables practical Markdown defaults for this vault.
- `.obsidian/core-plugins.json` turns on the core plugins you will use most.
- `.obsidian/templates.json` points the Templates plugin at `docs/templates`.
- `docs/templates/` contains reusable note templates for study sessions and daily notes.
- `docs/chapters_index.md` is the navigation hub for all chapters.
- `docs/obsidian_vault_architecture.md` defines the note architecture for the vault.
- `docs/research_papers_index.md` is the navigation hub for paper notes and paper folders.

## Open This Repo As A Vault

1. Open Obsidian.
2. Click **Open folder as vault**.
3. Select the repository root:

   `/media/jimmy/data_llm/llm_tutorials`

4. Let Obsidian index the files.

## Recommended Starting Notes

- Start from [README.md](../README.md) for the roadmap.
- Use [chapters_index.md](./chapters_index.md) for chapter navigation.
- Use [obsidian_vault_architecture.md](./obsidian_vault_architecture.md) for structure rules.
- Use [research_papers_index.md](./research_papers_index.md) for research-paper notes.
- Use [chapter_1/chapter_1_readme.md](../chapter_1/chapter_1_readme.md) for chapter-specific work.
- Use `docs/templates/chapter_session_template.md` when you study or implement something inside a chapter.
- Use `docs/templates/daily_note_template.md` for a daily log.

## Suggested Folder Usage

- Keep roadmap-wide navigation and architecture notes in `docs/`.
- Keep chapter hubs, chapter session notes, and chapter code in `chapter_n/`.
- Keep paper notes and paper files in `papers/`.
- Keep reusable templates in `docs/templates/`.
- Keep screenshots or pasted images in `docs/assets/`.

## First Obsidian Actions

1. Open `README.md`.
2. Open `docs/chapters_index.md`.
3. Open the active chapter hub.
4. Open the active session note in that chapter.
5. Use `Ctrl+O` to jump between notes quickly.
6. Use `[[double bracket links]]` to connect notes.

Example:

`[[README]]`

`[[docs/chapters_index]]`

`[[docs/research_papers_index]]`

`[[chapter_1/chapter_1_readme]]`

## How To Create A Note For Chapter Work

Use chapter-local notes so the repository stays organized and the vault graph stays predictable.

Examples:

- `chapter_1/session_01_notes.md`
- `chapter_2/runtime_observations.md`
- `chapter_4/rag_experiments.md`

Recommended naming style:

- lowercase
- underscores
- deterministic names

## How To Use Templates

1. Open the Command Palette with `Ctrl+P`.
2. Run `Templates: Insert template`.
3. Choose either:
   - `chapter_session_template`
   - `daily_note_template`
4. Fill in the placeholders.

## How To Link Your Learning Notes

Use links so your notes form a graph instead of isolated files.

Examples:

- Link a study note to the roadmap chapter:
  `Related roadmap: [[README]]`
- Link a session note to a chapter note:
  `Chapter anchor: [[chapter_1/chapter_1_readme]]`
- Link an implementation note to a Python entry point:
  `Code entry: main.py`

## A Good Daily Workflow

1. Open `README.md`.
2. Open `docs/chapters_index.md`.
3. Open `docs/research_papers_index.md` if you are reading papers.
4. Open the active chapter hub note.
5. Continue the active chapter session note, or create the next numbered session note if this is a new session.
6. Insert `chapter_session_template` when starting a new session note.
7. Study, code, and record decisions in the same note.
8. If progress changes, update the tracker with:

   `python3 docs/roadmap_tracker.py update ...`

9. Return to Obsidian and link the session note to the relevant chapter hub and roadmap.

## Useful Core Features

- File Explorer: browse your roadmap and chapter files.
- Search: find a concept or experiment across the vault.
- Backlinks: see which notes reference the current note.
- Outline: jump across headings in long notes.
- Graph View: visualize how chapter notes connect.
- Templates: create consistent study notes quickly.

## Practical Rules For This Vault

- Keep implementation notes near the matching chapter.
- Use `README.md` as the roadmap home, `docs/chapters_index.md` as the chapter navigator, and `chapter_n/chapter_n_readme.md` as the chapter hub.
- Use `docs/research_papers_index.md` and `papers/` for paper reading and summaries.
- Do not turn `docs/templates/` into a dumping ground for random notes.
- Use Obsidian for note structure and linking, but keep progress updates authoritative in `docs/roadmap_tracker.py`.
- Keep chapter readmes practical and aligned with the root roadmap.

## Recommended Next Step

Open the vault, pin `README.md`, `docs/chapters_index.md`, and `chapter_1/chapter_1_readme.md`, then continue `chapter_1/session_01_notes.md`.
