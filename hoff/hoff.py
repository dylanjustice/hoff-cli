from commands.dotnet import dotnet
import pkg_resources
import click

#region Commands

@click.group()
@click.option("-v", "--version", is_flag=True)
def main(version):
    """
        \b
        #    #       ####  #    # ######    ##### #    # ######    #    #  ####  ###### ###### ###
        #    #      #    # #    # #           #   #    # #         #    # #    # #      #      ###
        #    #      #    # #    # #####       #   ###### #####     ###### #    # #####  #####   #
        #    #      #    # #    # #           #   #    # #         #    # #    # #      #
        #    #      #    #  #  #  #           #   #    # #         #    # #    # #      #      ###
        #    ######  ####    ##   ######      #   #    # ######    #    #  ####  #      #      ###
        """

    if version:
        display_version()

main.add_command(dotnet)

#endregion Commands

#region Private Methods

def display_version():
    """Display the current version of the hoff-cli"""
    version = pkg_resources.require("hoff-cli")[0].version
    print("hoff-cli version:" + version)

#endregion Private Methods
