"""Helpers for Chapter 1 beginner LLM app framing."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class LearningFrame:
    """A simple description of a first LLM application."""

    app_name: str
    user_input: str
    prompt_sent_to_model: str
    model_job: str
    output: str
    assumptions: list[str] = field(default_factory=list)
    open_questions: list[str] = field(default_factory=list)


def default_learning_frame() -> LearningFrame:
    """Return a beginner-friendly starter frame for Chapter 1."""
    return LearningFrame(
        app_name="Simple LLM question-answer app",
        user_input="A user types a question in plain text.",
        prompt_sent_to_model="The program sends a short instruction plus the user's question.",
        model_job="Read the prompt and generate a helpful answer.",
        output="A plain-text answer shown back to the user.",
        assumptions=[
            "The first version only handles text input and text output.",
            "The first version should be easy to read before it is optimized.",
        ],
        open_questions=[
            "What exact use case should the first app solve?",
            "Should the first model be local or hosted?",
            "How should the answer be checked for quality?",
        ],
    )


def format_learning_frame(learning_frame: LearningFrame) -> str:
    """Render the learning frame as readable text."""
    assumptions = _format_bullets(learning_frame.assumptions)
    open_questions = _format_bullets(learning_frame.open_questions)

    return "\n".join(
        [
            f"App Name: {learning_frame.app_name}",
            f"User Input: {learning_frame.user_input}",
            f"Prompt Sent To Model: {learning_frame.prompt_sent_to_model}",
            f"Model Job: {learning_frame.model_job}",
            f"Output: {learning_frame.output}",
            "",
            "Assumptions:",
            assumptions,
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
