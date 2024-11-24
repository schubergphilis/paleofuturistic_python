# About

When it comes to helping others with developing software, too many templates/guides/peoples focus on features, or even worse, tools.
While this guided template extremely spotlights some tools, they are approached from a very different focus: needs.
Every software development project has almost identical needs:

- version control
- dependency management
- linting
- testing
- compiling
- documentation
- publishing

Of course, this list is not exhaustive.
Software development these days also needs CI/CD, SBOM exports, ergonomic chairs etc.
However, if anything from the list above is missing in your project, something is truly lacking.
With this template I'm trying to fill in those needs as simple yet effective as possible.

Some fanatics will look at this template and might say something like:
"Isn't pytest better than unittest?"
Or: "Isn't tox also super useful?"
Well, are those extra dependencies that will only really be useful to people who already know how to add them to this template?
Guess what, all three yes!

Also, is anyone still interested in the academic differences between linting and formatting?
No... until very weird errors start popping up and then you suddenly are...
Are you likely to get to that point on your first 1,000 commits?
No, and by that time, you can probably figure out how to stop that pesky formatter from undoing your intricacies.
(If you feel like getting into the weeds early though, [have at you](https://docs.astral.sh/ruff/configuration/).)

Similarly silly discussions can be had about Hatch, MkDocs or Sphinx.
I've had it with all these well-meaning 'developer advocates' forcing some tool on you at first chance, while no-one out there seems to be able to provide you a comprehensive end-to-end developer journey.
Also, by keeping the template simple, it's open to extension with your own favorite tools without carrying the bloat from my choices.

Anyway, despite my defensive stance, if you truly feel like you can make this template better without sacrificing its simplicity, by all means, make a pull request!
