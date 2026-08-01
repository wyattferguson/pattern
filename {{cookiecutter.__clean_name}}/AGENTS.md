# version: 0.2.0

## Stack

Python 3.13, uv, pytest, ruff, ty, taskipy

## Reply

- Be concise. Prioritize code and direct answers.
- Default to 1 short paragraph; use bullets only when content is inherently list-shaped.
- Use tables for stats and benchmarks.
- No recap, no praise, no filler, no narration.
- Prefer fragments over full prose where clarity is unchanged.
- Ask only for ambiguity, destructive ops, public API changes, secrets, or conflicting dirty worktree edits.

## Code

- Write pythonic code, type hints, docstrings, and absolute imports.
- Small functions, max line length 100 characters.
- Focused files, max 1000 lines.
- Validate changed code with Ruff, Ty, and relevant tests.
