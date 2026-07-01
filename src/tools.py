"""Tool registry for the Reasoning Agent."""


class ToolRegistry:
    """Registry of tools available to the ReAct agent.

    Tools are registered as callables with a name, description, and parameter schema.
    The registry handles lookup and execution.
    """

    def __init__(self):
        """Initialise an empty tool registry."""
        raise NotImplementedError("TODO: implement tool registry initialisation")

    def register(self, name: str, description: str, func: callable, parameters: dict) -> None:
        """Register a new tool.

        Args:
            name: Unique tool name.
            description: What the tool does.
            func: Callable that implements the tool.
            parameters: JSON Schema dict describing the tool's parameters.
        """
        raise NotImplementedError("TODO: implement tool registration")

    def execute(self, name: str, **kwargs) -> str:
        """Execute a registered tool by name.

        Args:
            name: The tool name.
            **kwargs: Arguments to pass to the tool function.

        Returns:
            The tool's string result.
        """
        raise NotImplementedError("TODO: implement tool execution from registry")

    def get_schemas(self) -> list[dict]:
        """Return Anthropic-format tool schemas for all registered tools.

        Returns:
            List of tool schema dicts for passing to Claude.
        """
        raise NotImplementedError("TODO: implement schema export")
