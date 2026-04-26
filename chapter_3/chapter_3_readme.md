# Chapter 3 - Learn Prompting Basics

Roadmap: [[README]]
Chapters: [[docs/chapters_index]]
Papers: [[docs/research_papers_index]]
Active Session: [[chapter_3/session_01_notes]]

## Goal

Learn how system instructions, user prompts, examples, and context change an LLM response.

## Concepts To Learn

- system message
- user prompt
- assistant response
- context
- output instructions
- few-shot examples
- prompt comparison

## Tools Or Libraries

- Python 3
- standard library only for the starter version

## Tasks

1. Read a prompt as separate message parts.
2. Compare a weak prompt with a clearer prompt.
3. Add context before asking the model to answer.
4. Practice simple output instructions.
5. Record what changed between prompt versions.

## Expected Outputs

- a small script that prints prompt variants
- deterministic mock responses for each variant
- short notes about which prompt was clearer and why

## Quick Exercises

1. Change one system instruction and run the script again.
2. Add one extra context sentence to the question-answering example.
3. Create one new prompt variant for extraction or summarization.

## Reference Book

- [Prompt Engineering for LLMs](https://www.oreilly.com/library/view/prompt-engineering-for/9781098156145/) by John Berryman and Albert Ziegler is the focused reference for this chapter.

## External Reference Details

- Source: [awesome-llm-books entry](https://github.com/Jason2Brownlee/awesome-llm-books/blob/main/books/prompt-engineering-for-llms.md)
- Repository: `Jason2Brownlee/awesome-llm-books`
- Title: Prompt Engineering for LLMs
- Subtitle: The Art and Science of Building Large Language Model-Based Applications
- Authors: John Berryman and Albert Ziegler
- Publisher: O'Reilly
- Publication date: 2024
- ISBN-13: 978-1098156152
- Pages: 280
- Best Chapter 3 reading focus: introduction to prompt engineering, moving to chat, prompt content, assembling the prompt, and taming the model.

## Files

- `main.py`: runs the Chapter 3 prompt comparison demo
- `utils.py`: stores prompt examples and helper functions
- `session_01_notes.md`: active session note for this chapter

## Notes

- Keep prompts short at first.
- Change only one thing at a time when comparing prompts.
- Treat context as input data, not as hidden magic.
