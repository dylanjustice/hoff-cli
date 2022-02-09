from dotnet import dotnet
import pkg_resources
import click


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
@main.command()
def version():
    """Display the current version of the hoff-cli"""
    version = pkg_resources.require("hoff-cli")[0].version
    print(version)

