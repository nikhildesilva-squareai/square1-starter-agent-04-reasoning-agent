"""ReActAgent: implements the Reasoning + Acting loop."""

from anthropic import Anthropic
from src.tools import ToolRegistry
from src.planner import decompose_question


class ReActAgent:
    """Agent that follows the ReAct pattern: Think -> Act -> Observe, repeating
    until it has enough information to produce a final answer.

    The agent maintains a scratchpad of its reasoning trace.
    """

    def __init__(
        self,
        tool_registry: ToolRegistry | None = None,
        client: Anthropic | None = None,
        model: str = "claude-sonnet-4-20250514",
        max_steps: int = 10,
    ):
        """Initialise the ReAct agent.

        Args:
            tool_registry: Registry of available tools. If None, create with defaults.
            client: Anthropic client instance. If None, create from env.
            model: Claude model identifier.
            max_steps: Maximum think-act-observe iterations before forcing an answer.
        """
        raise NotImplementedError("TODO: implement ReAct agent initialisation")

    def think(self, context: str) -> dict:
        """Generate the next thought and decide on an action.

        Args:
            context: The current scratchpad with all prior reasoning.

        Returns:
            A dict with:
            - 'thought': the agent's reasoning text
            - 'action': tool name to call, or 'finish' if done
            - 'action_input': arguments for the tool (dict), or final answer (str)
        """
        raise NotImplementedError("TODO: implement think step via Claude")

    def act(self, action: str, action_input: dict) -> str:
        """Execute the chosen action using the tool registry.

        Args:
            action: Tool name to execute.
            action_input: Arguments to pass to the tool.

        Returns:
            The observation (tool output) as a string.
        """
        raise NotImplementedError("TODO: implement action execution")

    def run(self, question: str) -> str:
        """Run the full ReAct loop on a question until completion.

        Args:
            question: The user's question.

        Returns:
            The agent's final answer string.
        """
        raise NotImplementedError("TODO: implement full ReAct loop (think-act-observe)")
