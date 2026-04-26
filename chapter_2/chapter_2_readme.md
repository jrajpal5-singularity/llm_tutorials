# Chapter 2 - Run Your First LLM

Roadmap: [[README]]
Chapters: [[docs/chapters_index]]
Papers: [[docs/research_papers_index]]
Active Session: [[chapter_2/session_01_notes]]

## Goal

Run the smallest possible LLM request flow and understand what goes in and what comes out.

## Concepts To Learn

- prompt
- response
- token at a high level
- local model vs hosted model
- response time

## Tools Or Libraries

- Python 3
- standard library only for the starter version

## Tasks

1. Understand the parts of a first LLM request.
2. Build a simple prompt from a system instruction and a user question.
3. Run the starter code with a mock model response.
4. Measure how long the response takes.
5. Identify what must change when moving from mock mode to a real provider.

## Expected Outputs

- a clear beginner-friendly first-run plan
- a working Python script that simulates the first request flow
- a short list of questions for the first real model integration

## Quick Exercises

1. Change the user question and run the script again.
2. Change the system instruction so the response should sound different.
3. Record the elapsed time for three runs and compare them.

## Files

- `main.py`: runs the Chapter 2 starter flow
- `utils.py`: stores the first-run data model and helper functions
- `session_01_notes.md`: active session note for this chapter
- `../papers/chapter_2/`: papers related to this chapter

## Notes

- Keep this chapter beginner-friendly.
- Start with the mock model flow before using a real provider.
- Focus on understanding the request path, not on optimization.
