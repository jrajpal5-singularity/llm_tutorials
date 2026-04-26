# Session 01

Roadmap: [[README]]
Chapter: [[chapter_2/chapter_2_readme]]
Papers: [[docs/research_papers_index]]

- Chapter: 2
- Date: 2026-04-23
- Focus: first LLM request flow and beginner Chapter 2 setup

## Goal

- Understand the smallest possible LLM request path.

## What I Studied

- The structure of a first LLM request.
- The difference between a mock response flow and a real provider flow.

## Key Concepts

- A prompt is what your program sends to the model.
- A response is what the model sends back.
- You can learn the request flow before connecting a real provider.

## Code Or Notes

- `chapter_2/main.py` prints the Chapter 2 plan and runs a mock demo.
- `chapter_2/utils.py` stores the first-run plan and helper functions.

## Decisions

- Chapter 2 will start with a deterministic mock model response.
- Quick exercises should be part of each chapter readme.

## Links

- `[[chapter_2/chapter_2_readme]]`
- `chapter_2/main.py`
- `chapter_2/utils.py`

## Session Timeline

- 2026-04-23 02:07 IST - Created the Chapter 2 scaffold and moved the active learning path to Chapter 2.
- 2026-04-25 16:03 IST - Checked the Chapter 2 quick exercises; exercise 2 still needs a changed system instruction and a mock response that can show the style difference.
- 2026-04-25 16:04 IST - Rechecked Chapter 2 after edits; the system instruction changed, but the mock response still ignores the prompt and answers an out-of-scope LLM question.
- 2026-04-25 16:35 IST - Rechecked Chapter 2 again; the code runs, but exercise 2 is still incomplete because the mock response ignores the prompt, and exercise 3 measures the artificial sleep delay.
- 2026-04-25 16:38 IST - Fixed the Chapter 2 quick exercise flow: the mock response now respects the fitness and health scope, and elapsed timing measures the mock model call instead of a delay between runs.

## Questions

- Which real provider should be used first after the mock flow makes sense?

## Next Step

- Run `python3 chapter_2/main.py` and inspect the request and response flow.
