def hello(someone: str = "you") -> str:
    """Greet someone.

    Parameters
    ----------
    someone : str, default='you'
        The name of the person to greet, by default 'you'

    Returns
    -------
    str
        A greeting message
    """
    return f"Hello {someone} from {{ cookiecutter.project_slug }}!"
