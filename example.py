"""
This is an example script that prints the flags
that you pass to it.
"""

import click

@click.command()
@click.option("--a", type=int, default=0)
@click.option("--b", type=int, default=0)
def main(a, b):
    print(f"a = {a}; b = {b}")

if __name__ == "__main__":
    main()
