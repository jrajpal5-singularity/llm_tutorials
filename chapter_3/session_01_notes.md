# Session 01

Roadmap: [[README]]
Chapter: [[chapter_3/chapter_3_readme]]
Papers: [[docs/research_papers_index]]

- Chapter: 3
- Date: 2026-04-26
- Focus: prompting basics and context engineering

## Goal

- Learn how prompt parts change the model response.

## What I Studied

- System instructions define response behavior.
- User prompts define the immediate task.
- Context gives the model information to answer from.
- Output instructions make the response shape more predictable.

## Key Concepts

- A weak prompt is vague and leaves the answer format unclear.
- A clear prompt gives task, context, and output expectations.
- Prompt comparison works best when changing one thing at a time.

## Code Or Notes

- `chapter_3/main.py` runs the prompt comparison demo.
- `chapter_3/utils.py` stores prompt examples and helper functions.
- Reference book: [Prompt Engineering for LLMs](https://www.oreilly.com/library/view/prompt-engineering-for/9781098156145/).
- Book source entry: [Jason2Brownlee/awesome-llm-books](https://github.com/Jason2Brownlee/awesome-llm-books/blob/main/books/prompt-engineering-for-llms.md).

## Decisions

- Chapter 3 starts with deterministic mock responses before using a real provider.
- The first examples cover summarization and question answering.

## Links

- `[[chapter_3/chapter_3_readme]]`
- `chapter_3/main.py`
- `chapter_3/utils.py`

## Session Timeline

- 2026-04-26 00:05 IST - Created the Chapter 3 scaffold for prompting basics and context engineering.
- 2026-04-26 00:06 IST - Verified `chapter_3/main.py` and selected Prompt Engineering for LLMs as the focused Chapter 3 reference book.
- 2026-04-26 00:10 IST - Updated Obsidian navigation notes so Chapter 3 is visible as the active chapter from the roadmap home and chapter index.
- 2026-04-26 00:29 IST - Added the awesome-llm-books repository details for Prompt Engineering for LLMs to the Chapter 3 hub and reference index.
- 2026-04-26 13:17 IST - Checked Chapter 3 results; the script runs and compiles, but `Summary:` is currently inserted into the prompt before `Assistant:`, which should be removed or renamed because it looks like an answer inside the input.
- 2026-04-26 13:18 IST - Rechecked Chapter 3 results; no code change yet, so the same `Summary:` issue and missing extraction/summarization variant remain.

## Questions

- Which prompt style creates the clearest answer for a beginner?

## Next Step

- Remove or rename the `Summary:` field in the generated prompt, then add one new extraction or summarization prompt variant.
