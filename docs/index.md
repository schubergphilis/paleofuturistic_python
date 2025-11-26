# Paleofuturistic Python

> _The Python development workflow your past self had always hoped for is finally here!_

<p align="center">
  <img src="./paleofuturistic_python.png?raw=true" alt="Paleofuturistic Environment"/>
</p>

This project is meant as an enterprise-ready template for developing Python packages.
If that bar is a bit too high for you, then you can checkout [Straight to the Money 💰](https://github.com/Carlovo/straight_to_the_money).
Paleofuturistic Python is a detached fork of Straight to the Money 💰.

## Usage

Prerequisite: [uv](https://docs.astral.sh/uv/)  
(Installing uv should also provide you with uvx.
Give their docs a look-over before continuing if you want to get a better understanding of what is going on under the hood in the steps below.)

### Setup

- Initialize with `uvx cruft create --checkout latest https://github.com/schubergphilis/paleofuturistic_python` and fill in your project details.
- Optional: validate the setup with `uv run python -c "import paleofuturistic_python; print(paleofuturistic_python.hello())"` (replace `paleofuturistic_python` with your project name/slug).
- Run `uv sync --all-extras --dev` to download the dependencies and generate a .lock file.

### Workflow

- Download dependencies (if you need any): `uv add some_lib_you_need`
- Develop (optional, tinker: `uvx --with-editable . ptpython`)
- QA:
    - Format: `uv run ruff format`
    - Lint: `uv run ruff check`
    - Type check: `uv run mypy`
    - Test: `uv run python -m unittest`
- Build: `uv build`
- Document: `uv run mkdocs build`
- Publish: `uv publish`

Can it really be that simple?
Well, eventually yes, but you will need to setup some connections and credentials still, of course.
For a slightly more elaborate walkthrough on that, see the [docs](walkthrough.md).
