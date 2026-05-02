
def use_plural(n: int, singular: str, plural: str | None = None, /) -> str:
    """
    *"Pluralizes a word based on the count."*

    Example:
        >>> _use_plural(1, 'transition')
        '1 transition'
        >>> _use_plural(3, 'transition')
        '3 transitions'
        >>> _use_plural(1, 'child', 'children')
        '1 child'
        >>> _use_plural(5, 'child', 'children')
        '5 children'

    Args:
        n (int): The count to determine singular or plural form.
        singular (str): The singular form of the word.
        plural (str | None, optional): The plural form of the word. If not provided, it defaults to the singular form with an 's' appended.

    Returns:
        str: A formatted string with the count and the correct singular or plural form of the word.
    """
    
    if n == 1:
        return f'{n} {singular}'
    return f'{n} {plural or singular + 's'}'

def use_brackets(text: str, color: str, *, lsymbol: str = '\\[', rsymbol: str = ']') -> str:
    return f'{color}{lsymbol}{text}{rsymbol}[/]'
