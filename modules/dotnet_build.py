import click
@click.command()
@click.option("-r", "--restore", is_flag=True)
@click.option("-c", "--clean", is_flag=True)
def dotnet_build():
    """"""
    print("building dotnet")