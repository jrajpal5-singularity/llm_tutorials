# Obsidian Vault Architecture

Roadmap: [[README]]
Chapters: [[docs/chapters_index]]

## Purpose

This vault is structured so learning notes, chapter plans, and runnable code stay aligned.

The design goal is simple:

- one roadmap home
- one navigation index
- one hub note per chapter
- one active session note per chapter session
- code stored beside the chapter notes it belongs to
- one dedicated papers area outside the chapter code folders

## Canonical File Roles

### 1. Roadmap Home

- File: `README.md`
- Purpose: top-level roadmap, phase ordering, tracker view, and project-wide entry point

### 2. Navigation Hub

- File: `docs/chapters_index.md`
- Purpose: navigate across chapters from one Obsidian note

### 3. Vault Architecture Note

- File: `docs/obsidian_vault_architecture.md`
- Purpose: define the note architecture so future work stays consistent

### 4. Research Papers Hub

- File: `docs/research_papers_index.md`
- Purpose: navigate paper notes and paper folders

### 5. Chapter Hub

- File pattern: `chapter_n/chapter_n_readme.md`
- Purpose: the authoritative note for a single chapter
- Contains: goal, concepts, tools, tasks, outputs, and links to code and sessions

### 6. Session Note

- File pattern: `chapter_n/session_nn_notes.md`
- Purpose: chronological working note for one real session
- Contains: focus, decisions, code changes, questions, blockers, and next steps

### 7. Chapter Code

- Files: `chapter_n/main.py`, `chapter_n/utils.py`
- Purpose: runnable code and helpers directly tied to that chapter

### 8. Research Papers Storage

- Folder: `papers/`
- Purpose: store paper notes and paper-related files outside the chapter code layout

## Folder Rules

- Keep chapter work inside `chapter_n/`.
- Keep project-wide architecture and navigation notes inside `docs/`.
- Keep templates inside `docs/templates/`.
- Keep pasted images and attachments inside `docs/assets/`.
- Keep research papers inside `papers/`.

## Linking Rules

- Every chapter hub should link back to `[[README]]`.
- Every session note should link to `[[README]]` and its chapter hub.
- Project-wide docs should link to the roadmap and chapters index.
- Paper notes should link to the roadmap and the related chapter when relevant.

## Naming Rules

- Use deterministic lowercase names.
- Session notes should use zero-padded numbering such as `session_01_notes.md`.
- Chapter hub notes must keep the exact name `chapter_n_readme.md`.
- Paper notes should use deterministic names such as `paper_001_<slug>.md`.

## Recommended Chapter Layout

```text
chapter_n/
  chapter_n_readme.md
  session_01_notes.md
  main.py
  utils.py
```

Optional additions only when needed:

- `data/`
- `assets/`
- `tests/`

## Research Papers Layout

```text
papers/
  shared/
  chapter_1/
  chapter_n/
```

Keep paper notes and paper files here so the chapter code stays simple.

## Recommended Workflow

1. Open `README.md`.
2. Open `docs/chapters_index.md`.
3. Open `docs/research_papers_index.md` if paper reading is part of the session.
4. Open the active `chapter_n/chapter_n_readme.md`.
5. Continue the active `session_nn_notes.md`.
6. Work in `main.py` and `utils.py`.
7. Update `docs/roadmap_tracker.py` when actual roadmap progress changes.

## Anti-Patterns

- Do not create random notes at the repository root.
- Do not mix project-wide notes into chapter folders unless they are truly chapter-specific.
- Do not spread one session across multiple differently named notes.
- Do not use Obsidian notes as the source of truth for progress tables when the tracker should be updated.
- Do not store research papers in arbitrary places when they belong in `papers/`.
