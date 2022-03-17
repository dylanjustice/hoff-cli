import click

from modules.echo import warn
from modules.node_clean import NodeClean
from modules.node_restore import NodeRestore
from modules.webpack_run import WebpackRun


@click.group("webpack")
def webpack():
    """Run various webpack commands for the project"""


@click.option("-c", "--clean", is_flag=True, help="Clean npm dependencies by removing node_modules in the working directory")
@click.option("-R", "--restore", is_flag=True, help="Restore npm dependencies (via npm install) in the current directory")
@click.argument("path", type=click.Path(exists=True), required=False)
@webpack.command()
def run(clean, restore, path):
    """Run project via npm run"""
    WebpackRun.run(clean, restore, path)


@webpack.command()
@click.argument("path", type=click.Path(exists=True), required=False)
def clean(path):
    """Clean npm dependencies by removing node_modules in the working directory"""
    NodeClean.run(path)


@click.option("--no-restore", help="Skip clean and restore the package prior to running a production build")
@webpack.command()
def publish():
    """Publishes a release build of the frontend project (via npm run build) in frontend"""
    warn("Command not yet implemented")


@click.option("--ci", is_flag=True, help="Clean and restore npm dependencies (via npm ci --no-optional) in the current directory")
@click.argument("path", type=click.Path(exists=True), required=False)
@webpack.command()
def restore(path, ci):
    """Restore npm dependencies (via npm install) in the current directory"""
    NodeRestore.run(path, ci)
