# -*- coding: utf-8 -*-

"""Console script for coinselectpy."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for coinselectpy."""
    click.echo("Replace this message by putting your code into "
               "coinselectpy.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
