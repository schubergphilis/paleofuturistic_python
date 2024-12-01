# Walkthrough

Some things in [usage](index.md#usage) might require a little more effort on the first run.
Let's go over those in more detail.

## Initializing your project

You will probably want to manage your project with some version control system and a remote, such as Git and GitHub.
Personally, I like creating the repository in the remote and then cloning to local.
That way everything is nicely set up for me.
Except for the template, of course.

[cruft](https://cruft.github.io/cruft/) ([cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) under its hood, actually) does not allow editing an existing directory by default for safety.
Because we just cloned an empty repository, we can assume to be safe though.
Clone your new repository somewhere.
From the directory directly above it run:
`uvx cruft create -f https://github.com/Carlovo/straight_to_the_money`
(mind the `-f`).
cd to your project directory; git add all, commit and push; and you are ready to go.

Other options would be:

- create the project with directory from the template with cruft, cd to it; git init, add all, commit, [set the remote](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#creating-remote-repositories) and push.
- create the project with directory from the template with cruft, copy the contents to a cloned repository; git add all, commit and push.

### Reviewing .gitignore and LICENSE

Are they superfluous in a minimal project template?
Maybe.
I would simply always add these two directly if they weren't there already, so adding them felt like a time-saver if only for myself.
If you had wanted another license than MIT, you have probably already chosen one and can easily override the templated one (if you do, do it in the `pyproject.toml` as well).
Maybe take a second look at the .gitignore, maybe not, it's fine...

## Previewing and publishing your documentation

So `uvx mkdocs build` nicely converts your documentation to a static website, now what?
You will probably want to preview it before committing the source files, and when committed you will probably want to publish the build files somewhere on the web.

MkDocs has two convenient commands build in for that:

- `uvx mkdocs serve` will serve a preview on local host `http://127.0.0.1:8000/` (with watch files!).
- `uvx mkdocs gh-deploy` will upload your documentation to GitHub Pages.

Both these commands have a lot of options and MkDocs has a lot more to offer in general (including automated publishing to other hosting parties).
[See for yourself.](https://www.mkdocs.org/)

## Publishing your Python package

It's all done; time to make your work available to the masses! `uv publish` can be configured to go a lot of places, but let's just admit PyPI is the standard.

For a fist time, it might be a good idea to use the [PyPI Test instance](https://test.pypi.org/) though.
Make an account there and get an api token.
Then you can upload your work with:  
`uv publish --publish-url https://test.pypi.org/legacy/ -t pypi-XXX`
(replace `XXX` with your specific credentials).

You can test whether everything went OK by running:  
`uv run --with "https://test-files.pythonhosted.org/packages/XXX/XXX/XXX/straight_to_the_money-0.1.0-py3-none-any.whl" --no-project -- python -c "import straight_to_the_money; print(straight_to_the_money.hello())"`
(replace `XXX` with your ids and `straight_to_the_money` to your project's name).

If that works or if you just want to skip to the real deal,
then make an account at [PyPI](https://pypi.org/) and
[configure uv](https://docs.astral.sh/uv/guides/publish/#publishing-your-package) to publish to it the proper way.

## Bonus: tinkering within context

My advice: run `uv add --dev ptpython`, then run `uv run ptpython` to bathe in luxury, and accept that you just pulled in couple of not strictly necessary dependencies.
You could simply run `uv run python` and tinker away in your virtual env, but quality of life in ptpython's REPL is simply much better.

Sadly, `uvx ptpython` doesn't work here.
It makes sense, of course, because uv's whole point is env separation.
Still, it would have been great in this particular case.
Maybe, hopefully, I can update this part someday with an elegant hack to make it possible.

## The updated happy path workflow

When you completed all the above successfully, pat yourself on the back for me.
The real reward is of course a reliable way of developing your Python project.
Considering the publishing and all, you may want to alter the workflow in this project's introduction to something like:

- Format: `uvx ruff format`
- Test: `uv run python -m unittest`
- Build: `uv build`
- Preview documentation: `uvx mkdocs serve`
- Publish package: `uv publish`
- Test package upload: `uv run --with "https://test-files.pythonhosted.org/packages/XXX/XXX/XXX/straight_to_the_money-0.1.0-py3-none-any.whl" --no-project -- python -c "import straight_to_the_money;`
- Publish documentation: `uvx mkdocs gh-deploy`

Or even better, create your own workflow that exactly caters to your project's needs.

Happy coding 🤗
