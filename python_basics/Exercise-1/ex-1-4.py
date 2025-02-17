import typer
from hello import say_hello

def main(names: list[str]):
    for name in names:
        print(say_hello(name))

typer.run(main)