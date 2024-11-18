# Straight to the Money 💰

Stop wasting time in analysis paralysis over Python tooling choices 💸  
Pick the defaults 💱  
Go straight to the money 💹

## Usage

Prerequisite: [uv](https://docs.astral.sh/uv/)

### Setup

- Initialize with `uvx cruft create https://github.com/Carlovo/straight_to_the_money` and fill in your project details.
- Validate the setup with `uv run python -c "import straight_to_the_money; print(straight_to_the_money.hello())"` (replace `straight_to_the_money` with your project name/slug).

### Workflow

- Format: `uvx ruff format`
- Test: `uv run python -m unittest`
