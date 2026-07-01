"""Question decomposition planner for the Reasoning Agent."""

from anthropic import Anthropic


def decompose_question(question: str, client: Anthropic | None = None) -> list[str]:
    """Decompose a complex question into a sequence of simpler sub-questions.

    Uses Claude to break down a multi-part or complex question into ordered
    steps that can each be answered independently and then combined.

    Args:
        question: The complex question to decompose.
        client: Anthropic client instance. If None, create from env.

    Returns:
        A list of sub-question strings in execution order.
    """
    raise NotImplementedError("TODO: implement question decomposition via Claude")
