# Beginner LLM Learning Roadmap

This roadmap is designed for a first-time LLM learner. It assumes no computer vision background and builds from the simplest useful LLM app toward retrieval, tools, serving, evaluation, and optimization.

## Current Focus

- Active chapter: [Chapter 3 - Learn Prompting Basics](chapter_3/chapter_3_readme.md)
- Active session note: [chapter_3/session_01_notes.md](chapter_3/session_01_notes.md)
- Next step: run `python chapter_3/main.py` and complete the quick prompt exercises.
- Reference book: [Prompt Engineering for LLMs](https://www.oreilly.com/library/view/prompt-engineering-for/9781098156145/) by John Berryman and Albert Ziegler.

## Table of Contents

- [Chapters Index](docs/chapters_index.md)
- [Obsidian Vault Architecture](docs/obsidian_vault_architecture.md)
- [Research Papers Index](docs/research_papers_index.md)
- [Current Focus](#current-focus)
- [Schedule Overview](#schedule-overview)
- [Progress Tracker](#progress-tracker)
- [Tracking Workflow](#tracking-workflow)
- [Obsidian Architecture](#obsidian-architecture)
- [Simple Project Structure](#simple-project-structure)
- [Research Papers](#research-papers)
- [Chapter 1 - Understand a Simple LLM App](#chapter-1---understand-a-simple-llm-app)
- [Chapter 2 - Run Your First LLM](#chapter-2---run-your-first-llm)
- [Chapter 3 - Learn Prompting Basics](#chapter-3---learn-prompting-basics)
- [Chapter 4 - Add Memory with RAG](#chapter-4---add-memory-with-rag)
- [Chapter 5 - Add Tools and Structured Output](#chapter-5---add-tools-and-structured-output)
- [Chapter 6 - Build a Small End-to-End App](#chapter-6---build-a-small-end-to-end-app)
- [Chapter 7 - Serve the App](#chapter-7---serve-the-app)
- [Chapter 8 - Check Quality and Reliability](#chapter-8---check-quality-and-reliability)
- [Chapter 9 - Optimize Only After It Works](#chapter-9---optimize-only-after-it-works)
- [Final Stack Map](#final-stack-map)
- [Total Timeline](#total-timeline)

## Schedule Overview

<!-- AUTO_SCHEDULE_NOTE_START -->
This schedule is anchored to your actual roadmap start date: `2026-04-26`. Future phase dates update from that starting point.
<!-- AUTO_SCHEDULE_NOTE_END -->

<!-- AUTO_SCHEDULE_START -->
| Phase | Chapter | Planned Start | Planned End | Duration |
| --- | --- | --- | --- | --- |
| Phase 0 | Understand a simple LLM app | 2026-04-26 | 2026-04-27 | 1-2 days |
| Phase 1 | Run your first LLM | 2026-04-28 | 2026-05-11 | 1-2 weeks |
| Phase 2 | Learn prompting basics | 2026-05-12 | 2026-05-25 | 1-2 weeks |
| Phase 3 | Add memory with RAG | 2026-05-26 | 2026-06-08 | 1-2 weeks |
| Phase 4 | Add tools and structured output | 2026-06-09 | 2026-06-15 | 1 week |
| Phase 5 | Build a small end-to-end app | 2026-06-16 | 2026-06-29 | 2 weeks |
| Phase 6 | Serve the app | 2026-06-30 | 2026-07-13 | 1-2 weeks |
| Phase 7 | Check quality and reliability | 2026-07-14 | 2026-07-20 | 1 week |
| Phase 8 | Optimize only after it works | 2026-07-21 | 2026-08-10 | 2-3 weeks |
<!-- AUTO_SCHEDULE_END -->

## Progress Tracker

The tracker is backed by `docs/roadmap_data.json` and can be updated with `docs/roadmap_tracker.py` so you do not have to edit these tables manually.

<!-- AUTO_PROGRESS_START -->
### Chapter Checklist

- [ ] Chapter 1 - Understand a simple LLM app
- [ ] Chapter 2 - Run your first LLM
- [ ] Chapter 3 - Learn prompting basics
- [ ] Chapter 4 - Add memory with RAG
- [ ] Chapter 5 - Add tools and structured output
- [ ] Chapter 6 - Build a small end-to-end app
- [ ] Chapter 7 - Serve the app
- [ ] Chapter 8 - Check quality and reliability
- [ ] Chapter 9 - Optimize only after it works

### Progress Table

| Phase | Chapter Target | Progress % | Status | Planned Start | Planned End | Actual Start | Actual End | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Phase 0 | Understand a simple LLM app | 0% | Not started | 2026-04-26 | 2026-04-27 |  |  |  |
| Phase 1 | Run your first LLM | 0% | Not started | 2026-04-28 | 2026-05-11 |  |  |  |
| Phase 2 | Learn prompting basics | 5% | In progress | 2026-05-12 | 2026-05-25 | 2026-04-26 |  | Run chapter_3/main.py and complete the quick prompt exercises. |
| Phase 3 | Add memory with RAG | 0% | Not started | 2026-05-26 | 2026-06-08 |  |  |  |
| Phase 4 | Add tools and structured output | 0% | Not started | 2026-06-09 | 2026-06-15 |  |  |  |
| Phase 5 | Build a small end-to-end app | 0% | Not started | 2026-06-16 | 2026-06-29 |  |  |  |
| Phase 6 | Serve the app | 0% | Not started | 2026-06-30 | 2026-07-13 |  |  |  |
| Phase 7 | Check quality and reliability | 0% | Not started | 2026-07-14 | 2026-07-20 |  |  |  |
| Phase 8 | Optimize only after it works | 0% | Not started | 2026-07-21 | 2026-08-10 |  |  |  |

### Recent Activity Log

| Log ID | Timestamp | Phase | Type | Ticket | Hours | Summary | Details |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PHASE-2-001 | 2026-04-26T00:05:00 | Phase 2 | update |  |  | Moved active work to Chapter 3 | Created Chapter 3 scaffold for prompting basics and context engineering. |
<!-- AUTO_PROGRESS_END -->

## Tracking Workflow

Use the Python tracker instead of editing progress by hand.

```bash
python3 docs/roadmap_tracker.py list
python3 docs/roadmap_tracker.py start-plan
python3 docs/roadmap_tracker.py show phase-2
python3 docs/roadmap_tracker.py update phase-2 --status "In progress" --progress 25 --summary "Started prompting study" --details "Reviewed prompt structure and context packing basics" --next-step "Build prompt comparison notebook" --ticket ROADMAP-12 --hours 1.5
python3 docs/roadmap_tracker.py log phase-2 --type blocker --summary "Dataset issue" --details "Need a better validation set" --ticket ROADMAP-12
python3 docs/roadmap_tracker.py sync-readme
```

The script automatically updates `actual_start`, `actual_end`, `progress_percent`, status, next steps, and a Jira-style activity log. If you begin work on a phase today, the script uses today's date and anchors the overall schedule from that point unless you override it.

## Obsidian Architecture

This repository is designed as an Obsidian-first learning vault, not just a code folder with Markdown files.

### Vault Roles

- `README.md`: roadmap home note and project entry point
- `docs/chapters_index.md`: chapter map and navigation hub
- `docs/obsidian_vault_architecture.md`: note architecture and file-role rules
- `chapter_n/chapter_n_readme.md`: chapter hub note for one chapter
- `chapter_n/session_nn_notes.md`: chronological session log for that chapter
- `chapter_n/main.py` and `chapter_n/utils.py`: runnable code and helpers for that chapter

### Working Rule

When you work on a chapter, open the roadmap, open the chapter hub, then continue the active session note in that same chapter folder.

## Simple Project Structure

This repository keeps the code path small on purpose.

```text
README.md
docs/
chapter_n/
papers/
```

Each chapter should start with only:

```text
chapter_n/
  chapter_n_readme.md
  session_01_notes.md
  main.py
  utils.py
```

Add more files only when the chapter actually needs them.

## Research Papers

Research papers have a separate place so they do not complicate the beginner code path.

```text
papers/
  shared/
  chapter_1/
```

- `papers/shared/` is for papers that matter across multiple chapters.
- `papers/chapter_n/` is for papers tied to one chapter.
- `docs/research_papers_index.md` is the note you use to navigate paper summaries.

## Chapter 1 - Understand a Simple LLM App

**Mapped Phase:** Phase 0

**Duration:** 1-2 days

### Learn

- The simplest flow: input -> prompt -> LLM -> answer
- What the model does
- What your Python program does

### Build

- A tiny text-based LLM app plan
- A simple representation of the app components

**Note:** No computer vision knowledge is needed here. Keep this chapter conceptual and simple.

## Chapter 2 - Run Your First LLM

**Mapped Phase:** Phase 1

**Duration:** 1-2 weeks

### Learn

- What a prompt is
- What a response is
- What a token is at a high level
- The difference between local and hosted models

### Tools

- A simple API client or local runtime

### Build

- Send your first prompt
- Print the model response
- Measure simple response time

**Why this matters:** You should see a model work before learning more advanced system details.

## Chapter 3 - Learn Prompting Basics

**Mapped Phase:** Phase 2

**Duration:** 1-2 weeks

### Learn

- System messages
- User prompts
- Output instructions
- Few-shot examples

### Build

- Summarization prompt
- Extraction prompt
- Question-answering prompt
- Compare prompt versions and note what changes help

**Why this matters:** Prompting is the first skill that improves results quickly.

## Chapter 4 - Add Memory with RAG

**Mapped Phase:** Phase 3

**Duration:** 1-2 weeks

### Learn

- Embeddings
- Chunking
- Retrieval
- Basic ranking

### Tools

- LlamaIndex or a simple vector store
- FAISS or Chroma

### Build

- Store documents
- Retrieve useful context
- Add context to the prompt

## Chapter 5 - Add Tools and Structured Output

**Mapped Phase:** Phase 4

**Duration:** 1 week

### Learn

- Structured output
- Tool calling
- Simple routing
- Basic state

### Tools

- Manual approach first
- LangChain only if needed

### Build

- LLM -> local tool or API -> answer

**Why this matters:** This is where the system becomes useful instead of just conversational.

## Chapter 6 - Build a Small End-to-End App

**Mapped Phase:** Phase 5

**Duration:** 2 weeks

### Learn

- Input handling
- Prompt building
- Model call flow
- Error handling

### Build

- Input layer
- Prompt assembly
- LLM reasoning
- Optional retrieval or tools
- Output or action

### End-to-End Flow

```text
Input -> prompt/context -> LLM -> output
```

**Why this matters:** This is the first point where everything works together as one small app.

## Chapter 7 - Serve the App

**Mapped Phase:** Phase 6

**Duration:** 1-2 weeks

### Learn

- API basics
- Request handling
- Basic logging
- Basic deployment ideas

### Tools

- FastAPI
- Docker (optional)

### Build

- Deploy an API
- Call the app through HTTP
- Measure basic performance

## Chapter 8 - Check Quality and Reliability

**Mapped Phase:** Phase 7

**Duration:** 1 week

### Learn

- Answer quality
- Hallucination checks
- Prompt quality
- Retrieval or tool-use quality

### Build

- A small checklist for outputs
- A simple evaluation script

**Why this matters:** This is where system quality becomes measurable rather than assumed.

## Chapter 9 - Optimize Only After It Works

**Mapped Phase:** Phase 8

**Duration:** 2-3 weeks

This phase comes last. Do not optimize early.

### 9.1 Basic Optimization

#### Learn

- Where time is spent
- Where memory is spent
- Model size vs speed
- Simple batching ideas

#### Do

- Measure before changing anything
- Compare a few simple runtime settings

### 9.2 Quantization

#### Learn

- FP16 vs BF16 vs INT8 vs INT4
- Accuracy vs latency tradeoff

#### Tools

- bitsandbytes
- TensorRT-LLM (optional, later)

#### Do

- Compare latency and memory before and after quantization

### 9.3 Advanced Optimization (Optional)

#### Learn

- More advanced runtime tuning
- Graph optimization
- Kernel fusion

#### Do

- Compare one advanced optimization path against the simpler baseline

**Note:** Skip this until the rest of the tutorial already makes sense.

### 9.4 Throughput and Memory

#### Learn

- GPU memory growth
- Request scheduling
- Throughput under multiple requests

#### Do

- Simulate a few concurrent requests
- Observe what gets slower

### 9.5 End-to-End Optimization

#### Learn

- Reduce unnecessary work
- Keep the request path simple
- Improve slow steps one at a time

#### Do

- Input -> retrieval/tools -> LLM -> output
- Remove obvious bottlenecks after measuring them

**Why this matters:** Optimization is useful only after you already have a working system you understand.

## Final Stack Map

| Layer | Tools |
| --- | --- |
| Runtime | API client or local runtime |
| Prompting | Prompt templates |
| Retrieval | RAG, LlamaIndex, FAISS/Chroma |
| Tools | Structured outputs, simple tool calling |
| System | FastAPI + simple app flow |
| Optimization | Quantization, runtime tuning |

## Total Timeline

### Realistic (with a job)

**10-14 weeks**

### Focused

**8-10 weeks**
