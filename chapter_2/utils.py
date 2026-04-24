"""Helpers for Chapter 2 first LLM run."""

from __future__ import annotations

from dataclasses import dataclass, field
from time import perf_counter


@dataclass(slots=True)
class FirstRunPlan:
    """A simple representation of a first LLM request flow."""

    provider_name: str
    model_name: str
    system_instruction: str
    user_question: str
    expected_output: str
    notes: list[str] = field(default_factory=list)
    open_questions: list[str] = field(default_factory=list)


def default_first_run_plan() -> FirstRunPlan:
    """Return a beginner-friendly starter plan for Chapter 2."""
    return FirstRunPlan(
        provider_name="mock provider",
        model_name="mock-llm-v1",
        system_instruction="You are a helpful assistant. Answer clearly and briefly.",
        user_question="What is an LLM?",
        expected_output="A short plain-text answer",
        notes=[
            "The starter version uses a mock response so the flow stays easy to understand.",
            "A real provider can be added later without changing the chapter structure.",
        ],
        open_questions=[
            "Which real provider should be used first?",
            "Should the first real model be local or hosted?",
            "How should prompt history be stored later?",
        ],
    )


def build_prompt(first_run_plan: FirstRunPlan) -> str:
    """Build a simple prompt from the system instruction and user question."""
    return (
        f"System: {first_run_plan.system_instruction}\n"
        f"User: {first_run_plan.user_question}\n"
        "Assistant:"
    )


def mock_model_response(prompt: str) -> str:
    """Return a deterministic mock response for the current prompt."""
    del prompt
    return "An LLM is a language model trained to predict and generate text."


def run_mock_demo(first_run_plan: FirstRunPlan) -> str:
    """Run the prompt through the mock model and report elapsed time."""
    prompt = build_prompt(first_run_plan)
    started_at = perf_counter()
    response = mock_model_response(prompt)
    elapsed_ms = (perf_counter() - started_at) * 1000

    return "\n".join(
        [
            f"Provider: {first_run_plan.provider_name}",
            f"Model: {first_run_plan.model_name}",
            f"Prompt: {prompt}",
            f"Response: {response}",
            f"Elapsed (ms): {elapsed_ms:.3f}",
        ]
    )


def format_first_run_plan(first_run_plan: FirstRunPlan) -> str:
    """Render the plan as readable text."""
    notes = _format_bullets(first_run_plan.notes)
    open_questions = _format_bullets(first_run_plan.open_questions)

    return "\n".join(
        [
            f"Provider Name: {first_run_plan.provider_name}",
            f"Model Name: {first_run_plan.model_name}",
            f"System Instruction: {first_run_plan.system_instruction}",
            f"User Question: {first_run_plan.user_question}",
            f"Expected Output: {first_run_plan.expected_output}",
            "",
            "Notes:",
            notes,
            "",
            "Open Questions:",
            open_questions,
        ]
    )


def _format_bullets(items: list[str]) -> str:
    """Format a list of strings as bullet lines."""
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)
