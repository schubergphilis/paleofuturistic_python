# Walkthrough

Some things in [usage](index.md#usage) might require a little more effort on the first run.
Let's go over those things and the rest in a little more detail.

## Initializing your project

You will probably want to manage your project with some version control system and a remote, such as Git and GitHub.
Personally, I like creating the repository in the remote and then cloning to local.
That way everything is nicely set up for me.
Except for the template, of course.

[cruft](https://cruft.github.io/cruft/) ([cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) under its hood) does not allow editing an existing directory by default for safety.
Because we just cloned an empty repository, we can assume to be safe though.
Clone your new repository somewhere.
From the directory directly above it run:
`uvx cruft create -f --checkout latest https://github.com/schubergphilis/paleofuturistic_python`
(mind the `-f`).
cd to your project directory; git add all, commit and push; and you are ready to go.

Other options would be:

- create the project with directory from the template with cruft, cd to it; git init, add all, commit, [set the remote](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#creating-remote-repositories) and push.
- create the project with directory from the template with cruft, copy the contents to a cloned repository; git add all, commit and push.

### Reviewing .gitignore and LICENSE

If you had wanted another license than Apache, you have probably already chosen one and can easily override the templated one (if you do, do it in the `pyproject.toml` as well).
Maybe take a second look at the .gitignore, maybe not, it's fine...

## Dependency management

Usually a lot or even more of the low-level functionality you need for what you want to develop is already available.
Luckily, reeling that good stuff in is one of uv's strengths.
To download all dependencies to get started properly run `uv sync --all-extras --dev`.
The `--all-extras --dev` flags trigger downloading optional and development dependencies respectively.
After that you can add dependencies like `uv add requests`.

These commands do everything you would hope they to do by default.
Yes, that includes caching and project-based isolation.
For starters just adding some dependencies from PyPI is probably all you want.
All the other things you would want from (uv's) dependency management you can always look into later.

By now you might have already guessed that uv acts on dependencies in your environment and uvx is meant for tools that live outside of it.

Just a reminder: add the names of the public features you develop to the `__all__` list in `__init__.py`.
This way others (that includes your unittest runs) can conveniently access them upon importing the module.

## Quality assurance (formatting, linting, type checking and testing)

You can see the config for these steps in the `pyproject.toml`.
Formatting (`uv run ruff format`), type checking (`uv run mypy`) and testing (`uv run python -m unittest`) should speak for themselves.
The ruff formatter, mypy and Python's build-in testing library are ubiquitous and easy to use.

You can get into the weeds very fast with linting (`uv run ruff check`) though.
If you go with the flow of this template it's probably going to work out fine for your first 1,000 commits or so.
And by that time you can probably figure out how to stop a pesky linter from undoing your intricacies,
so my advice would be to not give it too much thought.
(If you feel like getting into the weeds early though, [have at you](https://docs.astral.sh/ruff/configuration/).)

## Building your package

uv has its own build backend nowadays.
It works only for pure Python projects at the moment, but that's probably good enough for most projects.
If you have more special needs you probably already know what you want and can configure that in the `pyproject.toml`.

Other than that, this step should simply be a `uv build` command that just works.

## Previewing and publishing your documentation

So `uvx --with mkdocstrings[python] mkdocs build` nicely converts your documentation to a static website...
Now what and what is that magic `--with` statement?
First the `--with`, it injects additional dependencies into the environment for mkdocs, in this case mkdocstrings with its python add-on.
Run the command and check you project's documentation to see the fancy feature descriptions mkdocstrings can make for you from a docstring.
(I found mkdocstrings works best with numpy style docs, so that's the template's default; you can change that in the `mkdocs.yaml`.)

Wait, how do I check my documentation and how do I publish it?
MkDocs has two convenient commands build in for that:

- `uvx --with mkdocstrings[python] mkdocs serve` will serve a preview on local host `http://127.0.0.1:8000/` (with watch files!).
- `uvx --with mkdocstrings[python] mkdocs gh-deploy` will upload your documentation to GitHub Pages.

Both these commands have a lot of options and MkDocs has a lot more to offer in general (including automated publishing to other hosting parties).
[See for yourself.](https://www.mkdocs.org/)

## Publishing your Python package

It's all done; time to make your work available to the masses!
`uv publish` can be configured to go a lot of places, but let's just admit PyPI is the standard.

While you can make an account at [PyPI](https://pypi.org/),
download a credential
and [configure uv](https://docs.astral.sh/uv/guides/publish/#publishing-your-package) to publish that way,
it might be a better a idea to replace the credentials with [configuring a trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).
If you follow trusted publisher guide you only have to change the owner and repository name from the example to make the release flow of this template work.

Afterwards run `uv run --isolated --no-project --with paleofuturistic_python python -c "import paleofuturistic_python; print(paleofuturistic_python.hello())"` to test whether everything went OK
(replace `paleofuturistic_python` to your project's slug).

### Security considerations

Note you have just bestowed great power upon GitHub.
With great power comes... No wait we have something serious to say here!

If you followed the guides linked above you will have already setup a separate GitHub env for publishing and made use of PyPI's trusted publishing.
That's great, but it's advisable to put up an even higher fence against attacks.

You can for example use the following settings to protect your repository from outsiders:

- Protect at least the `main` branch and `v*` tags with rulesets; configure them to enforce updates via peer-reviewed pull requests from forks.
- Enable "Limit to users explicitly granted read or higher access" under "Code review limits".
- Set "Require approval for all external contributors" under "Actions permissions" -> "Approval for running fork pull request workflows from contributors".
- Set "Read repository contents and packages permissions" (no default repo write) under "Actions permissions" -> "Workflow permissions".
- Uncheck "Allow GitHub Actions to create and approve pull requests" under "Actions permissions" -> "Workflow permissions".
- You could even go as far as setting "Temporary interaction limits" under "Interaction limits".

Protecting your repository from insider threats is far harder, but this might help:

- Set some "Required reviewers" under "Environments" -> "Deployment protection rules".
- Cumbersome to implement, but effective: org/repo admin access only for non-personal accounts which require 4-eyes approval for assuming.

## Bonus: tinkering within context

You could simply run `uv run python` and tinker away in your virtual env, but quality of life in ptpython's REPL is simply much better.
Directly running `uvx ptpython` doesn't work here, because uv's whole point is env separation.
To give your current project's context to ptpython you can run `uvx --refresh --with . ptpython`.
The `--refresh` is added to flush uv's cache so your most recent edits are also usable in ptpython.

## The updated happy path workflow

When you completed all the above successfully, pat yourself on the back for me.
The real reward is of course a reliable way of developing your Python project.
Considering the publishing and all, you may want to alter the workflow in this project's introduction to something like:

- Download dependencies (if you need any): `uv add some_lib_you_need`
- Develop (optional, tinker: `uvx --refresh --with . ptpython`)
- QA:
    - Format: `uv run ruff format`
    - Lint: `uv run ruff check` (or simply `uv run ruff check --fix` if, you also, like to live dangerously)
    - Type check: `uv run mypy`
    - Test: `uv run python -m unittest`
- Build: `uv build` (just to test it works)
- Preview documentation: `uvx --with mkdocstrings[python] mkdocs serve`
- Publish package: kickoff the Publish to PyPI workflow in GitHub Actions
- Publish documentation: `uvx --with mkdocstrings[python] mkdocs gh-deploy`

Or even better, create your own workflow that exactly caters to your project's needs.

Happy coding 🤗
