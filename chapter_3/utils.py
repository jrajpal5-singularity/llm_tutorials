"""Helpers for Chapter 3 prompting basics."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class PromptExample:
    """A small prompt example for comparing prompt behavior."""

    name: str
    system_instruction: str
    user_prompt: str
    context: list[str] = field(default_factory=list)
    output_instruction: str = ""
    summary: str = ""


def default_prompt_examples() -> list[PromptExample]:
    """Return beginner-friendly prompt examples for Chapter 3."""
    return [
        PromptExample(
            name="weak_summary_prompt",
            system_instruction="You are a helpful assistant whose task is to chat.",
            user_prompt="Summarize this.",
            context=[
                "LLM apps usually send instructions, user input, and optional context to a model.",
                "Clear prompts make the expected answer easier for the model to follow.",
            ],
            summary="This is about LLM apps and prompts.",
        ),
        PromptExample(
            name="clear_summary_prompt",
            system_instruction="You are a concise tutor for a beginner LLM learner.",
            user_prompt="Summarize the context in two short bullet points.",
            context=[
                "LLM apps usually send instructions, user input, and optional context to a model.",
                "Clear prompts make the expected answer easier for the model to follow.",
            ],
            output_instruction="Use exactly two bullets.",
            summary="This is a clear and concise summary of the context.",
        ),
        PromptExample(
            name="question_answering_prompt",
            system_instruction="Answer only from the provided context.",
            user_prompt="What parts are sent to the model in a basic LLM app?",
            context=[
                "A basic LLM app sends a system instruction, a user prompt, and sometimes extra context.",
                "The system instruction guides the model's behavior, the user prompt contains the user's input, and the context provides additional information that can help the model generate a better response.",
            ],
            output_instruction="If the context is not enough, say that the context is not enough.",
            summary="The app sends a system instruction, a user prompt, and sometimes extra context.",
        ),
    ]


def build_prompt(example: PromptExample) -> str:
    """Build one readable prompt from message-like parts."""
    lines = [f"System: {example.system_instruction}"]

    if example.context:
        lines.append("Context:")
        lines.extend(f"- {item}" for item in example.context)

    lines.append(f"User: {example.user_prompt}")

    if example.output_instruction:
        lines.append(f"Output Instruction: {example.output_instruction}")
    lines.append(f"Summary: {example.summary}")
    lines.append("Assistant:")
    return "\n".join(lines)


def mock_llm_response(example: PromptExample) -> str:
    """Return a deterministic response that changes with prompt clarity."""
    if example.name == "weak_summary_prompt":
        return "This is about LLM apps and prompts."
    if example.name == "clear_summary_prompt":
        return "\n".join(
            [
                "- LLM apps send instructions, user input, and optional context to a model.",
                "- Clear prompts make the desired answer easier to follow.",
            ]
        )
    if example.name == "question_answering_prompt":
        return "The app sends a system instruction, a user prompt, and sometimes extra context."
    return "No mock response is defined for this prompt example."


def compare_prompt_variants(examples: list[PromptExample]) -> list[dict[str, str]]:
    """Build prompts and deterministic responses for comparison."""
    comparisons = []
    for example in examples:
        comparisons.append(
            {
                "name": example.name,
                "prompt": build_prompt(example),
                "response": mock_llm_response(example),
            }
        )
    return comparisons


def format_comparison(comparisons: list[dict[str, str]]) -> str:
    """Format prompt comparisons as readable console output."""
    sections = []
    for comparison in comparisons:
        sections.append(
            "\n".join(
                [
                    f"Example: {comparison['name']}",
                    "Prompt:",
                    comparison["prompt"],
                    "Mock Response:",
                    comparison["response"],
                ]
            )
        )
    return "\n\n---\n\n".join(sections)
