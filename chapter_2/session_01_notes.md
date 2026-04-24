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

## Questions

- Which real provider should be used first after the mock flow makes sense?

## Next Step

- Run `python3 chapter_2/main.py` and inspect the request and response flow.
