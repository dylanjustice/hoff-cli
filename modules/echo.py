import click

prefix = click.style(f"[hoff]:", fg="magenta")
error_prefix = click.style(f"[ERROR]", fg="red")


def info(message):
    if message is None:
        return
    click.echo("{0} {1}".format(prefix, message))

def error(message):
    if message is None:
        return
    click.echo("{0} {1} {2}".format(prefix, error_prefix, message))

def success(message):
    if message is None:
        return
    message = click.style(f"{message}", fg="bright_green")
    click.echo("{0} {1}".format(prefix,message))