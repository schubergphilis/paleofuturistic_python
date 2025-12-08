# Walkthrough

Some things in [usage](index.md#usage) might require a little more effort on the first run.
Let's go over the bootstrapping and the development cycle in full detail.

In this walkthrough we are going to create a Python library and publish it to PyPI.
While doing so we will do all the steps you would normally do during feature development as well.
Also, we will publish the project's documentation to GitHub Pages.

You are encouraged to go through this walkthrough twice.
Upon first run, only execute the instructions and ignore all the explanations underneath.
Then reread this page in full to get a better grasp of what this template is setting up for you.

## Initializing your project

Instructions:

- Create a repository in GitHub;
  do not add any additional files upon creation, like .gitignore, LICENSE etc.;
  make sure you take a project name not already on PyPI, if you want to follow this walkthrough all the way to publishing there;
  make sure you make the repo public, if you want to follow this walkthrough all the way to publishing the documentation on GitHub Pages.
- Clone the repo to your development environment.
- Execute this command from the directory directly above: `uvx cruft create -f --checkout latest https://github.com/schubergphilis/paleofuturistic_python`.
- Answer the questions; `project_slug` should be the same as the GitHub repository name you chose.
- cd to your project directory; execute `git add --all` and `git commit -m "chore: initial commit"`.
- Execute `uv sync --all-extras --dev`;
  this gives multiline output and should state something about having downloaded and installed a lot of packages successfully.
- Execute `git add --all` and `git commit -m "chore: lock initial dependencies"`.
- Do not git push yet!
  This would trigger CI which we will cover later.

### Managing boilerplate

[cruft](https://cruft.github.io/cruft/) ([cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) under its hood) is a tool for managing boilerplate.
New projects can be instantiated from a template with it, like you did above.
An even more amazing function is that it can update a project's boilerplate when the template changes (also this Paleofuturistic one!).
See the [extra guides](extra_guides.md#update-your-paleofuturistic-boilerplate) for more information on that.

It might still be noteworthy to point out a few things in the command you used:
`uvx cruft create -f --checkout latest https://github.com/schubergphilis/paleofuturistic_python`.
The `--checkout latest` in there should speak for itself.
Now mind the `-f`.
cruft does not allow editing an existing directory by default for safety.
Because we just cloned an empty repository, we can assume to be safe though.

Other options to get to the same state would be:

- create the project with directory from the template with cruft, cd to it; git init, add all, commit, [set the remote](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#creating-remote-repositories) and push.
- create the project with directory from the template with cruft, copy the contents to a cloned repository; git add all, commit and push.

### Reviewing .gitignore and LICENSE

If you had wanted another license than Apache, you have probably already chosen one and can easily override the templated one (if you do, do it in the `pyproject.toml` as well).
Maybe take a look at the .gitignore, maybe not; it's fine; I promise.

### Dependency management

Usually a lot or even more of the low-level functionality you need for what you want to develop is already available.
Luckily, reeling that good stuff in is one of uv's strengths.
The `--all-extras --dev` flags from the uv command above triggers downloading optional and development dependencies respectively.
After that you can add dependencies like for example `uv add requests` or `uv add --dev pytest` for dev dependencies.

These commands do everything you would hope they would do by default.
Yes, that includes caching and project-based environment isolation.
For starters just adding some dependencies from PyPI is probably all you want.
All the other things you would want from (uv's) dependency management you can always look into later.

By now you might have already guessed that uv acts on dependencies in your environment and uvx is meant for tools that live outside of it.

> A reminder: add the names of the public features you develop to the `__all__` list in `src/<YOUR_PROJECT_SLUG>/__init__.py`.
> This way others (that includes your unittest runs) can conveniently access them upon importing your module.

## Quality assurance

Instructions:

- Execute `uv run ruff format --diff`; should output `4 files already formatted`.
- Execute `uv run ruff check`; should output `All checks passed!`.
- Execute `uv run mypy`; should output `Success: no issues found in 2 source files`.
- Execute `uv run python -m unittest`; gives multiline output, should end with `OK`.
- Execute `git status`; gives multiline output, should end with `nothing to commit, working tree clean`.

### Formatting, linting, type checking and testing

The steps above are the minimal steps to assure quality in any software project.
When they output that everything is as expected, they should also leave the codebase unchanged.
The dependencies for these steps are pinned in the `pyproject.toml` to make sure they run the same way locally as in the pipeline.
The pipeline can run quite quickly upon repetition, because caching is enabled, see `.github/workflows/quality_assurance.yaml`.

Formatting (`uv run ruff format --diff`), type checking (`uv run mypy`) and testing (`uv run python -m unittest`) should speak for themselves.
The ruff formatter, mypy and Python's build-in testing library are ubiquitous and easy to use.
Only mypy has a minimal amount of config in the `pyproject.toml` that makes it a bit more specific and tight.

You can get into the weeds very fast with linting (`uv run ruff check`) though.
If you go with the flow of this template it's probably going to work out fine for your first 1,000 commits or so.
And by that time you can probably figure out how to stop a pesky linter from undoing your intricacies,
so my advice would be to not give it too much thought.
(If you feel like getting into the weeds early though, [have at you](https://docs.astral.sh/ruff/configuration/).)

Small thing worth mentioning is that the `pyproject.toml` is set up such that the ruff linter and formatter should not contradict each other.
Also, the activated linting rules are a little more than the default, mainly because isort is really convenient.

## Building your package

Instructions:

- Execute `uv build`;
  gives multiline output, should end with `Successfully built dist/<YOUR_PROJECT_SLUG>-0.0.0-py3-none-any.whl`.
- Execute `git status`;
  gives multiline output, should end with `nothing to commit, working tree clean`.

### The artifacts to distribute

uv has its own build backend nowadays.
It works only for pure Python projects at the moment, but that's probably good enough for most projects.
If you have more special needs you probably already know what you want and can configure that under `[build-system]` in the `pyproject.toml`.
Also, uv is not so sure the build backend won't significantly change in the future.
For that reason there is an upper limit in the `pyproject.toml` on uv's minor version as per their best practices.
(If you ever update uv beyond that version and this breaks your build step for that reason, check back on this template and [update](extra_guides.md#update-your-paleofuturistic-boilerplate).)

Other than that, this step should simply be a `uv build` command that just works.
Locally you will probably only run this command to validate it works though.
Eventually the project's pipelines should build and publish for you.

## Previewing your documentation

Instructions:

- Execute `uv run mkdocs build`;
  gives multiline output, should end with `INFO    -  Documentation built in <X> seconds`.
- Execute `uv run mkdocs serve`;
  gives multiline output, should end with `INFO    -  <X> Serving on http://127.0.0.1:8000/`;
- Navigate to `http://127.0.0.1:8000/`;
  some rudimentary documentation should be there.
- Get back to the command-line in your local clone;
  terminate the serving process.
- Execute `git status`;
  gives multiline output, should end with `nothing to commit, working tree clean`.

### A very feature-rich static website

In your project directory go to `docs/index.md` and see how little was needed to produce such a fantastic skeleton for documentation.
(Of course, you do need to keep every relevant docstring nice and tidy to make that work.)
I found mkdocstrings works best with numpy style docs, so that's the template's default.
You can change that and more in the `mkdocs.yaml`.
Don't try to understand all of that at once...

MkDocs offers far more than everything you accomplished above, especially combined with even more plugins.
[See for yourself.](https://www.mkdocs.org/)
Personal favorite out of the box: watch files.
Others might particularly like automated publishing to other documentation hosting parties than GitHub Pages.

## Continuous integration

Instructions:

- Navigate to `https://github.com/settings/personal-access-tokens`.
- Generate a new token;
  it should have access "Read and Write" on "Contents" and "Pull requests" on ONLY the repository you are working with now,
  this will also automatically grant access "Read-only" on "Metadata".
- Go to `https://github.com/<YOUR_GITHUB_HANDLE>/<YOUR_PROJECT_SLUG>/settings/environments/new` and create an environment called `release-please`.
- Set "Deployment branches and tags" to only allow branch `main` to use the new environment.
- Set `RELEASE_PLEASE_TOKEN` as an environment secret with the token you just generated.
- Get back to the command-line in your local clone.
- Execute `git commit --allow-empty -m "feat: release initial version"` and `git push`.
- Navigate to `https://github.com/<YOUR_GITHUB_HANDLE>/<YOUR_PROJECT_SLUG>/actions`;
  see that the "Quality Assurance CI" and "Release Please" workflows succeed.
- Go to `https://github.com/<YOUR_GITHUB_HANDLE>/<YOUR_PROJECT_SLUG>/pull/1`;
  see that Release Please created a pull request for you.

### Release orchestration

The quality assurance was already covered above.
Having it in the CI helps keeping the main branch up to specs.
A small side note is that the quality assurance CI also includes building the package and documentation.
Whether this is part of QA or not is debatable, but it's clear you don't want to find build errors in your release pipelines.

This template sets up your project to use [Release Please Action](https://github.com/googleapis/release-please-action) as release orchestrator.
This unburdens you from updating the toml and lock files for each release, and remembering to update the documentation website.
It also keeps a nice changelog and of course it creates GitHub releases.

If you want Release Please to keep a nice looking changelog for you, then you have to be a little disciplined in naming your commits.
Release Please expects commits to adhere to [Conventional Commits](https://www.conventionalcommits.org/).
This is a good idea anyway, so that should be a reasonable demand.
(When merging commits into the main branch with pull requests, it is probably easiest to make the PR title adhere to Conventional Commits and to 'squash merge'.)

Sadly, Release Please does require a dedicated GitHub token to operate, because actions triggered from pull requests are too limited for this template when operating with the default GitHub token.
The token is something quite sensitive to manage, because it breaks those (security) limits, but worth that effort.
Be especially careful on new workflows that create toxic permission combinations which allow pull requests from strangers to escalate privileges.
See the [extra guides](extra_guides.md#github-security-enhancements) on some more tips on securing your repository.

## Publishing to PyPI and GitHub Pages

- Navigate to `https://github.com/<YOUR_GITHUB_HANDLE>/<YOUR_PROJECT_SLUG>/settings/environments/new` and create an environment called `pypi`.
- Set "Deployment branches and tags" to only allow tags `v*` to use the new environment.
- Go to [PyPI](https://pypi.org/) and login;
  if you have no account there, create one first.
- Configure a [trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).
- Go to `https://github.com/<YOUR_GITHUB_HANDLE>/<YOUR_PROJECT_SLUG>/settings/pages` set "Source" to "GitHub Actions".
- Go to `https://github.com/<YOUR_GITHUB_HANDLE>/<YOUR_PROJECT_SLUG>/pull/1` and approve and (squash) merge the pull request.
- Go to `https://github.com/<YOUR_GITHUB_HANDLE>/<YOUR_PROJECT_SLUG>/actions`;
  a GitHub Action should be running to create a GitHub release.
- Wait for the workflows to finish, then two other GitHub workflows should spawn triggered by the creation the release;
  these actions should publish you package on PyPI and publish your documentation on GitHub Pages.
- Wait until all actions finish.
- Go to `https://github.com/<YOUR_GITHUB_HANDLE>/<YOUR_PROJECT_SLUG>/releases`;
  note that a release has been created.
- Get back to the command-line in your local clone.
- Execute `git pull`;
  note that a changelog was created and some versioning numbers were updated.
- Navigate to `https://<YOUR_GITHUB_HANDLE>.github.io/<YOUR_PROJECT_SLUG>/`;
  it should display the same documentation you served locally in the previous part.
- Get back to the command-line in your local clone.
- Execute `uv run --isolated --no-project --with <YOUR_PROJECT_SLUG> python -c "from <YOUR_PROJECT_SLUG> import hello; print(hello())"`;
  should output `Hello you from <YOUR_PROJECT_SLUG>!`.

### Beyond v0.1.0

If all of the above worked, congratulations!
Of course you are not reading this for just celebration, but you wanted to know more about what happened under the hood.

uv supports publishing from/to anywhere with credentials.
But, if possible, publishing with a trusted publisher unburdens you from credential management.

In the `release.yaml`, note caching is explicitly disabled.
This makes the release step more dependable, because by accident wrong dependencies could end up in the cache.
Also deliberately by the way, so this is also a security measure.
If you want to know more, lookup something like: GitHub Actions cache poisoning.

Setting the `pypi` environment did not add security in the steps above.
You can (and should) use it for that way though.
This walkthrough is getting very long already, so more on how to set that up is in the [extra guides](extra_guides.md#github-security-enhancements).

Also in the extra guides you can find the [minimal steps](extra_guides.md#executable-apps) on how to build and publish a CLI from this template.
Unless your project will be really simple (which it never will be), I would advise to make separate lib and app/cli projects for business logic and integration respectively.
Otherwise you could just use a simple [script with inline dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).

## Bonus: the ptpython REPL

- Get back to the command-line in your local clone.
- Execute `uvx --with-editable . ptpython`;
  you should now be in ptpython's REPL.
- Type `from <YOUR_PROJECT_SLUG> import hello` and enter;
  note the hinting and coloring to help you.
- Type `hello(someone="me")` and enter;
  should output `'Hello me from <YOUR_PROJECT_SLUG>!'`.
- Execute `exit()` to exit the REPL.

### Tinkering within context  

You could simply run `uv run python` and tinker away in your virtual env, but quality of life in ptpython's REPL is simply much better.
Directly running `uvx ptpython` doesn't work here, because uv's whole point is env separation.
To give your current project's context to ptpython you can run `uvx --with-editable . ptpython`.
`--with-editable` is used instead of `--with` to make uv look at the latest local updates of your code (including its dependencies!).

## The updated happy path workflow

When you completed all the above successfully, pat yourself on the back for me.
The real reward is of course a reliable way of developing your Python project.

Now that you went through all the bootstrapping needed only once, your development happy flow may look something like this:

- Download dependencies (if you need any): `uv add some_lib_you_need`
- Develop (optional, tinker: `uvx --with-editable . ptpython`)
- QA:
    - Format: `uv run ruff format` (or `uv run ruff format --diff` if you want to check the proposed changes first)
    - Lint: `uv run ruff check` (or simply `uv run ruff check --fix` if, you also, like to live dangerously)
    - Type check: `uv run mypy`
    - Test: `uv run python -m unittest`
- Build: `uv build` (just to test it works)
- Preview documentation: `uv run mkdocs serve`
- Publish package and docs: approve the `chore(main): release x.x.x` pull request from Release Please

Or even better, create your own workflow that exactly caters to your project's needs.

Happy coding 🤗
