"""Chapter 3 entry point for prompting basics."""

from utils import compare_prompt_variants, default_prompt_examples, format_comparison


def main() -> None:
    """Run the Chapter 3 prompt comparison demo."""
    examples = default_prompt_examples()
    comparisons = compare_prompt_variants(examples)

    print("Chapter 3 - Prompting Basics")
    print()
    print(format_comparison(comparisons))


if __name__ == "__main__":
    main()
