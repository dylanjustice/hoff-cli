import pkg_resources
import click

from commands.dotnet import dotnet
from commands.copy import copy
from commands.webpack import webpack

# region Commands


@click.group()
def main():
    """
        \b
        #    #       ####  #    # ######    ##### #    # ######    #    #  ####  ###### ###### ###
        #    #      #    # #    # #           #   #    # #         #    # #    # #      #      ###
        #    #      #    # #    # #####       #   ###### #####     ###### #    # #####  #####   #
        #    #      #    # #    # #           #   #    # #         #    # #    # #      #
        #    #      #    #  #  #  #           #   #    # #         #    # #    # #      #      ###
        #    ######  ####    ##   ######      #   #    # ######    #    #  ####  #      #      ###
        """


main.add_command(dotnet)
main.add_command(copy)
main.add_command(webpack)


@main.command()
def version():
    """Display the current version of the hoff-cli"""
    version = pkg_resources.require("hoff-cli")[0].version
    click.echo(message="[hoff-cli] version: " + version, color=True)

# endregion Commands
