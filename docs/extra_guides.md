# Extra guides

## Update your Paleofuturistic boilerplate

If this template gets updated and you want to benefit from the new features, follow the steps below:

- Go to the command-line in your local clone of your project.
- Execute `uvx cruft update --checkout latest`.
- The steps after that should be self-explanatory, but there is always [more information available for those who want](https://cruft.github.io/cruft/#updating-a-project).

## GitHub security enhancements

Note you have just bestowed great power upon GitHub.
With great power comes... No wait we have something serious to say here!

If you followed the complete walkthrough from this template you will have already set up a separate GitHub env for publishing and made use of PyPI's trusted publishing.
That's great, but it's advisable to put up an even higher fence against attacks.

You can for example use the following settings to protect your repository from outsiders:

- Protect at least the `main` branch and `v*` tags with rulesets;
  for example enforce updates via peer-reviewed pull requests on `main`, and forbid deleting and editing tags.
- Enable "Limit to users explicitly granted read or higher access" under "Code review limits".
- Set "Require approval for all external contributors" under "Actions permissions" -> "Approval for running fork pull request workflows from contributors".
- You could even go as far as setting "Temporary interaction limits" under "Interaction limits".

Protecting your repository from insider threats is far harder, but this might help:

- Set some "Required reviewers" under "Environments" -> "Deployment protection rules".
- Cumbersome to implement, but effective: org/repo admin access only for non-personal accounts which require 4-eyes approval for assuming.

Protecting your repository is important, even more so when it's hooked up to CI/CD.
GitHub security is a subject by itself.
Do not just rely on the checklist above.
Think about your own situation, and implement the checks and balances you think are necessary.
As always, the internet can help you with thinking.

## Executable apps

> You may need to flush uv's cache after implementing the code below before the commands will work.

This workflow template was created for libraries, because those are usually the most involved to get going.
Making the template able to produce Python apps is not much work luckily.
(Making stand-alone apps is a whole other story though!
In that case you may want to look at [PyInstaller](https://pyinstaller.org/) or [Nuitka](https://nuitka.net/) for example.)

To make the package an executable module that supports something like `uv run python -m <YOUR_PROJECT_SLUG>` create a `src/<YOUR_PROJECT_SLUG>/__main__.py` that looks something like:

``` Python
from <YOUR_PROJECT_SLUG> import hello


def main() -> None:
    print(hello())


if __name__ == "__main__":
    main()
```

Then to make tools like uvx and pipx be able to execute the module like so `uvx --with-editable . <YOUR_PROJECT_SLUG>` add the following to the `pyproject.toml`.

``` toml
[project.scripts]
<YOUR_PROJECT_SLUG> = "<YOUR_PROJECT_SLUG>.__main__:main"
```

After publishing your package to PyPI a simple `uvx <YOUR_PROJECT_SLUG>` should do.
(And `uv run --isolated --no-project --with <YOUR_PROJECT_SLUG> python -m <YOUR_PROJECT_SLUG>` coming back to the example above.)

If you are setting out to build an app, you can implement all the boilerplate yourself with `os` and `argparse`.
You could also look into available frameworks, for example for CLIs: [Typer](https://typer.tiangolo.com/).
