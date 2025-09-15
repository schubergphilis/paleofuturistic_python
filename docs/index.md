# Paleofuturistic Python

> _The Python development workflow your past self had always hoped for is finally here!_

<p align="center">
  <img src="./paleofuturistic_python.png?raw=true" alt="Paleofuturistic Environment"/>
</p>

This is a detached fork of [Straight to the Money 💰](https://github.com/Carlovo/straight_to_the_money).
Check it out if this template is a bit too involved for you and you want to go with something more simple.

## Usage

Prerequisite: [uv](https://docs.astral.sh/uv/)  
(Installing uv should also provide you with uvx.
Give their docs a look-over before continuing if you want to get a better understanding of what is going on under the hood in the steps below.)

### Setup

- Initialize with `uvx cruft create --checkout latest https://github.com/schubergphilis/paleofuturistic_python` and fill in your project details.
- Optional: validate the setup with `uv run python -c "import paleofuturistic_python; print(paleofuturistic_python.hello())"` (replace `paleofuturistic_python` with your project name/slug).
- Either, run `uv lock` to generate a .lock file, or run `uv add some_lib_you_need` if your project has dependencies.

### Workflow

- Download dependencies (if you need any): `uv add some_lib_you_need`
- Develop (optional, tinker: `uvx --refresh --with . ptpython`)
- QA:
    - Format: `uvx ruff format`
    - Lint: `uvx ruff check`
    - Type check: `uvx mypy`
    - Test: `uv run python -m unittest`
- Build: `uv build`
- Document: `uvx --with mkdocstrings[python] mkdocs build`
- Publish: `uv publish`

Can it really be that simple?
Well, eventually yes, but you will need to set up some connections and credentials still, of course.
For a slightly more elaborate walkthrough on that, see the [docs](https://schubergphilis.github.io/paleofuturistic_python/walkthrough/).

Still skeptical?
See the [about](https://schubergphilis.github.io/paleofuturistic_python/about/) instead.
Or, have a look at [a kitchen sink project](https://github.com/carlovoSBP/kitchen_sink_full_of_cravings) created with this template.
