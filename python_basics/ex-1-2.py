import typer
from hello import say_hello

def main(name: str):
    print(say_hello(name))

typer.run(main)