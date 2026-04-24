"""Chapter 2 entry point for a first beginner LLM run."""

from utils import default_first_run_plan, format_first_run_plan, run_mock_demo


def main() -> None:
    """Print the plan and run a mock first LLM request."""
    first_run_plan = default_first_run_plan()
    print(format_first_run_plan(first_run_plan))
    print()
    print("Mock Run:")
    print(run_mock_demo(first_run_plan))


if __name__ == "__main__":
    main()
