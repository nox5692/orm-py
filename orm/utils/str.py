import re


def camel_to_snake(s: str):
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    snake = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return snake.lower()
