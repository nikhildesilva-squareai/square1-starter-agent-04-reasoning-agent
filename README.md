# Multi-Step Reasoning Agent — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · LLM Agent Architect · Project 4.**

🤖 **Agent project.** This repo provides the project scaffold, function stubs, and contract tests. Read the full brief on Square 1 for guidance.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# P4: Multi-Step Reasoning Agent

Build a ReAct (Reasoning + Acting) agent that decomposes complex questions into steps, uses tools to gather information, and reasons through intermediate results to produce a final answer.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # Add your ANTHROPIC_API_KEY
```

## Usage

```bash
python -m src.cli
```

## Project Structure

```
src/
  reasoning.py  - ReActAgent with think/act/observe loop
  tools.py      - Tool registry and execution
  planner.py    - Question decomposition
  cli.py        - Interactive command-line interface
tests/
  test_agent.py - Contract tests for reasoning pipeline
```
