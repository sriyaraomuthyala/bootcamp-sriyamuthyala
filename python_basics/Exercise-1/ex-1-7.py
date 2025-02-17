import typer
import logging
from say_hello_with_config import say_hello
from logging_config import setup_logging

def main(names: list[str], log: bool = False):
    if log:
        setup_logging()
    for name in names:
        logging.info(f"Saying hello to {name}")
        print(say_hello(name))

typer.run(main)
