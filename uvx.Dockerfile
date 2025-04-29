FROM node:18
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/