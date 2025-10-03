# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Usage

Legacy: `pip install {{ cookiecutter.project_slug }}`

Preferred: `uv add {{ cookiecutter.project_slug }}`

## Developing further

> Development flow as [Paleofuturistic Python](https://github.com/schubergphilis/paleofuturistic_python)

Prerequisite: [uv](https://docs.astral.sh/uv/)

### Setup

- Clone this repository.
- Download additional dependencies: `uv sync --all-extras --dev`
- Optional: validate the setup with `uv run python -m unittest`

### Workflow

- Download dependencies (if you need any): `uv add some_lib_you_need`
- Develop (optional, tinker: `uvx --refresh --with . ptpython`)
- QA:
    - Format: `uv run ruff format`
    - Lint: `uv run ruff check`
    - Type check: `uv run mypy`
    - Test: `uv run python -m unittest`
- Build (to validate it works): `uv build`
- Review documentation updates: `uvx --with mkdocstrings[python] mkdocs serve`
- Make a pull request.
