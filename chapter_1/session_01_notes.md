# Session 01

Roadmap: [[README]]
Chapter: [[chapter_1/chapter_1_readme]]
Papers: [[docs/research_papers_index]]

- Chapter: 1
- Date: 2026-04-23
- Focus: understand Chapter 1 Python structure and dataclasses

## Goal

- Understand what a dataclass is and why it is used in `chapter_1/utils.py`.

## What I Studied

- What `@dataclass` does in Python.
- How `LearningFrame` stores the app structure in one object.

## Key Concepts

- A dataclass is a convenient way to group related data in one class.
- It automatically creates boilerplate like an `__init__` method.
- It is useful when a class mainly stores data rather than complex behavior.

## Code Or Notes

- `LearningFrame` in `chapter_1/utils.py` is a dataclass.
- It stores fields like `app_name`, `user_input`, and `model_job` in one structured object.
- `field(default_factory=list)` is used so each instance gets its own list.

## Decisions

-

## Links

- `[[chapter_1/chapter_1_readme]]`
- `chapter_1/utils.py`

## Session Timeline

- 2026-04-23 01:58 IST - Explained what dataclasses are using `LearningFrame` in `chapter_1/utils.py`.

## Questions

- When should a normal class be used instead of a dataclass?

## Next Step

- Learn how `default_learning_frame()` creates a dataclass instance and how `format_learning_frame()` reads from it.
