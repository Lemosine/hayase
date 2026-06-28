# Hayase
testing test
Build the first working slice of this project.

## Current status

This repository has a starter Python project skeleton. The first goal is to keep the shape small, testable, and easy to grow.

## Project notes

- Keep secrets out of git. Use `config.example.json` as the public template.
- Keep the first working slice simple before adding background services or automation.
- Use this only with feeds, files, and content you have permission to access.

## Local development

```bash
python -m pip install -e .
python -m pytest
python -m hayase
```
