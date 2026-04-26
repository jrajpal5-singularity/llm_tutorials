"""Chapter 1 entry point for a simple beginner LLM app."""

from utils import default_learning_frame, format_learning_frame


def main() -> None:
    """Print the current Chapter 1 learning frame."""
    learning_frame = default_learning_frame()
    print(format_learning_frame(learning_frame))


if __name__ == "__main__":
    main()
