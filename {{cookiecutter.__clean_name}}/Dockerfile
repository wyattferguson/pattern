# --- Builder stage ---
# Use the official uv image (based on Debian Bookworm slim) as the build environment.
# uv is used to resolve and install dependencies into a virtual environment.
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

# Compile .pyc bytecode at install time so the runtime image starts faster,
# and copy files into the venv instead of symlinking (required for multi-stage copies).
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

WORKDIR /app

# Copy only the files needed to resolve dependencies first.
# This allows Docker to cache the dependency-install layer independently of source changes.
COPY pyproject.toml uv.lock README.md ./
# Install dependencies (excluding dev extras and the project itself) using the cache mount
# to speed up repeated builds without storing the cache in the image layer.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

# Copy the project source code, then install the project itself into the venv.
COPY src/ ./src/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


# --- Runtime stage ---
# Use a minimal Python image without uv or build tools to keep the final image small.
FROM python:3.13-slim

WORKDIR /app

# Copy only the virtual environment and source from the builder stage,
# leaving behind uv, caches, and any other build-time artifacts.
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src

# Prepend the venv's bin directory to PATH so the venv's Python and scripts are used.
ENV PATH="/app/.venv/bin:$PATH"

# Run the project's main module as the container's default command.
CMD ["python", "-m", "{{cookiecutter.__clean_slug}}.{{cookiecutter.__clean_slug}}"]
