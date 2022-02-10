from dotnet import dotnet
import pkg_resources
import click

#region Commands

@click.group(invoke_without_command=True)
@click.option("-version", "--version", is_flag=True)
def main(version):
    if version:
        display_version()
        pass

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

#endregion Commands

#region Private Methods

def display_version():
    """Display the current version of the hoff-cli"""
    version = pkg_resources.require("hoff-cli")[0].version
    print(version)

#endregion Private Methods
