# Crave all the Money 🤑

> _Open source Python project template with enterprise-level teamwork in mind_

Don't settle for less than a Python project template that fulfils all your development needs 🤝  
Don't settle for less than a Python project template that uses the best tools 🛠️  
Crave all the money 🤑

This is a detached fork of [Straight to the Money 💰](https://github.com/Carlovo/straight_to_the_money).
Check it out if this template is a bit too involved for you and you want to go with something more simple.

## Usage

Prerequisite: [uv](https://docs.astral.sh/uv/)  
(Installing uv should also provide you with uvx.
Give their docs a look-over before continuing if you want to get a better understanding of what is going on under the hood in the steps below.
Also look at their docs for the parts of dependency management not covered in this template's standard flow, such as removing dependencies from your project.)

### Setup

- Initialize with `uvx cruft create --checkout latest https://github.com/carlovoSBP/crave_all_the_money` and fill in your project details.
- Optional: validate the setup with `uv run python -c "import crave_all_the_money; print(crave_all_the_money.hello())"` (replace `crave_all_the_money` with your project name/slug).
- Either, run `uv lock` to generate a .lock file, or run `uv add some_lib_you_need` if your project has dependencies.

### Workflow

- Format: `uvx ruff format`
- Test: `uv run python -m unittest`
- Build: `uv build`
- Document: `uvx mkdocs build`
- Publish: `uv publish`

Can it really be that simple?
Well, eventually yes, but you will need to set up some connections and credentials still, of course.
For a slightly more elaborate walkthrough on that, see the [docs](https://carlovosbp.github.io/crave_all_the_money/walkthrough/).

Still skeptical?
See the [about](https://carlovosbp.github.io/crave_all_the_money/about/) instead.
Or, have a look at [my kitchen sink project](https://github.com/carlovoSBP/kitchen_sink_full_of_cravings) created with this template.
