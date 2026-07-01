"""Contract tests for the Multi-Step Reasoning Agent.

These tests verify the public interface of each module.
They are expected to FAIL against the stubs and PASS once implemented.
"""

import pytest
from src.planner import decompose_question
from src.reasoning import ReActAgent


class TestPlanner:
    """Question decomposition must produce actionable steps."""

    def test_question_decomposition_produces_steps(self):
        """decompose_question() returns a list of at least 2 sub-questions."""
        steps = decompose_question(
            "What is the GDP of France and how does it compare to Germany's?"
        )
        assert isinstance(steps, list)
        assert len(steps) >= 2
        assert all(isinstance(s, str) and len(s) > 0 for s in steps)


class TestReActThink:
    """The think step must return a structured action decision."""

    def test_think_returns_valid_action(self):
        """think() returns a dict with thought, action, and action_input."""
        agent = ReActAgent()
        result = agent.think("Question: What is 2+2?\nScratchpad: (empty)")
        assert isinstance(result, dict)
        assert "thought" in result
        assert "action" in result
        assert "action_input" in result


class TestReActLoop:
    """The full reasoning loop must terminate and produce an answer."""

    def test_full_reasoning_loop_terminates(self):
        """run() returns a non-empty string answer and doesn't loop forever."""
        agent = ReActAgent()
        answer = agent.run("What is the capital of Australia?")
        assert isinstance(answer, str) and len(answer) > 0
