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
For example `uv add requests` does everything you would hope it to do by default.
Yes, that includes caching and project-based isolation.
For starters just adding some dependencies from PyPI is probably all you want.
All the other things you would want from (uv's) dependency management you can always look into later.

## Quality assurance (formatting, linting, type checking and testing)

You can see the config for these steps in the `pyproject.toml`.
Formatting (`uvx ruff format`), type checking (`uvx mypy`) and testing (`uv run python -m unittest`) should speak for themselves.
The ruff formatter, mypy and Python's build-in testing library are ubiquitous and easy to use.

You can get into the weeds very fast with linting (`uvx ruff check`) though.
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

So `uvx mkdocs build` nicely converts your documentation to a static website, now what?
You will probably want to preview it before committing the source files, and when committed you will probably want to publish the build files somewhere on the web.

MkDocs has two convenient commands build in for that:

- `uvx mkdocs serve` will serve a preview on local host `http://127.0.0.1:8000/` (with watch files!).
- `uvx mkdocs gh-deploy` will upload your documentation to GitHub Pages.

Both these commands have a lot of options and MkDocs has a lot more to offer in general (including automated publishing to other hosting parties).
[See for yourself.](https://www.mkdocs.org/)

## Publishing your Python package

It's all done; time to make your work available to the masses!
`uv publish` can be configured to go a lot of places, but let's just admit PyPI is the standard.

For a first time, it might be a good idea to use the [PyPI Test instance](https://test.pypi.org/) though.
Make an account there and get an api token.
Then you can upload your work with:  
`uv publish --publish-url https://test.pypi.org/legacy/ -t pypi-XXX`
(replace `XXX` with your specific credentials).

You can test whether everything went OK by running:
`uv run --with "https://test-files.pythonhosted.org/packages/XXX/XXX/XXX/paleofuturistic_python-0.1.0-py3-none-any.whl" --no-project -- python -c "import paleofuturistic_python; print(paleofuturistic_python.hello())"`
(replace `XXX` with your ids and `paleofuturistic_python` to your project's name).

If that works or if you just want to skip to the real deal,
then make an account at [PyPI](https://pypi.org/) and
[configure uv](https://docs.astral.sh/uv/guides/publish/#publishing-your-package) to publish to it the proper way.

## Bonus: tinkering within context

You could simply run `uv run python` and tinker away in your virtual env, but quality of life in ptpython's REPL is simply much better.
Directly running `uvx ptpython` doesn't work here, because uv's whole point is env separation.
To give your current project's context to ptpython you can run `uvx --with . ptpython`.

## The updated happy path workflow

When you completed all the above successfully, pat yourself on the back for me.
The real reward is of course a reliable way of developing your Python project.
Considering the publishing and all, you may want to alter the workflow in this project's introduction to something like:

- Download dependencies (if you need any): `uv add some_lib_you_need`
- Develop (optional, tinker: `uvx --with . ptpython`)
- QA:
    - Format: `uvx ruff format`
    - Lint: `uvx ruff check` (or simply `uvx ruff check --fix` if, you also, like to live dangerously)
    - Type check: `uvx mypy`
    - Test: `uv run python -m unittest`
- Build: `uv build`
- Preview documentation: `uvx mkdocs serve`
- Publish package: `uv publish`
- Publish documentation: `uvx mkdocs gh-deploy`

Or even better, create your own workflow that exactly caters to your project's needs.

Happy coding 🤗
