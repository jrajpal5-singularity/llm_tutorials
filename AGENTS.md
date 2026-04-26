# AGENTS.md

## Purpose

This file defines the working guardrails for this repository.

The project is a structured roadmap for learning and building LLM systems directly. Work in this repository should stay aligned with the roadmap in [README.md](/media/jimmy/data_llm/llm_tutorials/README.md) and the tracker files in [docs/roadmap_tracker.py](/media/jimmy/data_llm/llm_tutorials/docs/roadmap_tracker.py) and [docs/roadmap_data.json](/media/jimmy/data_llm/llm_tutorials/docs/roadmap_data.json).

## Project Guardrails

1. Keep the repository chapter-oriented. New learning or implementation work should be grouped by chapter.
2. Do not create random top-level scripts for chapter work. Chapter work belongs inside `chapter_n/`.
3. Use deterministic names so future automation stays simple and predictable.
4. Prefer small, readable Python modules over one large script.
5. Keep chapter README files practical and deterministic. The README filename for each chapter must be `chapter_n_readme.md`.
6. If progress changes, prefer updating it through `docs/roadmap_tracker.py` rather than editing tracker sections in `README.md` manually.
7. Use ASCII by default unless a file already requires non-ASCII text.
8. Preserve existing files unless the user explicitly asks to replace or remove them.
9. Treat this repository as an Obsidian vault as well as a code repository.
10. For substantive chapter work, keep the relevant Obsidian note updated during the work session instead of only summarizing at the end.
11. When updating Obsidian notes, add concise timestamped entries using local repository time in a deterministic format such as `2026-04-23 01:27 IST`.
12. Follow the Obsidian-first file architecture defined in `docs/obsidian_vault_architecture.md`.
13. Assume the learner may be new to both LLMs and computer vision unless the user says otherwise.
14. Keep chapter code as small and beginner-friendly as possible.

## Chapter Creation Contract

When the user says `make chapter_1`, `make chapter_2`, or generally `make chapter_n`, interpret that as a request to scaffold a new chapter folder with a standard structure.

The folder name must be:

- `chapter_n`

Examples:

- `make chapter_1` -> create `chapter_1/`
- `make chapter_4` -> create `chapter_4/`

## Required Output For `make chapter_n`

When creating a chapter, always create these files:

- `chapter_n/chapter_n_readme.md`
- `chapter_n/main.py`
- `chapter_n/utils.py`

If the chapter already exists, do not overwrite user work blindly. Read the existing files first and then extend them safely.

## Chapter README Requirements

`chapter_n/chapter_n_readme.md` should contain:

1. Chapter title
2. Goal of the chapter
3. Concepts to learn
4. Tools or libraries for the chapter
5. Tasks or implementation steps
6. Expected outputs
7. Quick exercises that can be finished quickly after the chapter
8. Notes section for progress or observations

Keep the chapter README directly tied to the corresponding roadmap chapter in the root `README.md`.

## Python File Requirements

### `chapter_n/main.py`

Use this as the main runnable entry point for the chapter.

It should usually include:

- a module docstring
- a `main()` function
- a standard `if __name__ == "__main__":` entry point

### `chapter_n/utils.py`

Use this for helper functions shared by chapter scripts.

Do not put unrelated project-wide logic here.

## Optional Files

Create these only when needed by the user request or by the chapter scope:

- `chapter_n/data/`
- `chapter_n/assets/`
- `chapter_n/notes.md`
- `chapter_n/tests/`

Do not create optional folders by default unless they are useful for the requested chapter.

Project-wide non-chapter exception:

- `papers/` is reserved for research paper notes and paper-related files.

## Obsidian Note Workflow

When chapter work is active, maintain a chapter-local Markdown note so the learning trail stays current inside Obsidian.

Preferred behavior:

1. Reuse the existing active session note for the chapter when one already exists.
2. If no suitable session note exists and the work is substantial, create a deterministic note such as `chapter_n/session_01_notes.md` or the next matching session file.
3. Append short timestamped updates as work progresses, not just at the end of the task.
4. Capture decisions, code changes, questions, and next steps in the note.
5. Keep the note concise and practical; avoid turning it into a raw terminal log.
6. Keep chapter notes inside `chapter_n/` unless the note is clearly project-wide and belongs in `docs/`.
7. Do not manually treat Obsidian notes as the source of truth for roadmap status when `docs/roadmap_tracker.py` should be updated instead.

## Obsidian Architecture Rules

Use these file roles consistently:

1. `README.md` is the roadmap home note.
2. `docs/chapters_index.md` is the navigation hub across chapters.
3. `docs/obsidian_vault_architecture.md` defines the vault structure and naming rules.
4. `docs/research_papers_index.md` is the navigation note for research papers.
5. `chapter_n/chapter_n_readme.md` is the hub note for one chapter.
6. `chapter_n/session_nn_notes.md` is the chronological session note for one chapter session.
7. `chapter_n/main.py` and `chapter_n/utils.py` are the canonical code files for the chapter unless the chapter scope clearly needs more modules.
8. `papers/` stores paper notes and paper files outside the chapter code folders.

When editing or creating notes, preserve this hierarchy instead of inventing new top-level note patterns.

## Simplicity Rule

Prefer the smallest structure that still teaches clearly:

1. Keep each chapter executable with `main.py` and `utils.py` unless more files are clearly necessary.
2. Do not introduce extra abstraction layers early in the tutorial.
3. Explain concepts as if the learner is seeing LLM application structure for the first time.
4. Put research reading in `papers/` instead of complicating the chapter code layout.

Recommended timestamp style for note entries:

- `2026-04-23 01:27 IST - Explained SystemFrame dataclass in utils.py.`
- `2026-04-23 01:31 IST - Updated launch.json to open external URLs during debug output.`

## Chapter Content Rule

When scaffolding `chapter_n`, align the content with the roadmap chapter:

- `chapter_1` -> target system framing
- `chapter_2` -> LLM runtime core
- `chapter_3` -> prompting and context engineering
- `chapter_4` -> RAG memory layer
- `chapter_5` -> tool calling and control
- `chapter_6` -> full system pipeline
- `chapter_7` -> serving and deployment
- `chapter_8` -> evaluation and reliability
- `chapter_9` -> hardware and throughput optimization

## Behavior For Future Agent Work

When asked to create a chapter:

1. Create `chapter_n/`
2. Create `chapter_n/chapter_n_readme.md`
3. Create `chapter_n/main.py`
4. Create `chapter_n/utils.py`
5. Fill the README and Python files with chapter-specific starter content
6. Keep the content minimal but usable
7. Do not add unrelated dependencies unless the user asks

During normal chapter work beyond scaffolding:

1. Read the active chapter note or session note before extending it.
2. Continue updating that note in the background while implementing or explaining work.
3. Add timestamps to meaningful note updates so the sequence of work remains clear in Obsidian.
4. Reflect important implementation changes and open questions in the note before finishing the task.

## Example Interpretation

If the user says:

- `make chapter_1`

The expected action is:

- create `chapter_1/`
- create `chapter_1/chapter_1_readme.md`
- create `chapter_1/main.py`
- create `chapter_1/utils.py`
- populate them with starter content for target system framing
