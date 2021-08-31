"""Usage: dotnet [options]
Usage: dotnet [path-to-application]

Options:
  -h|--help         Display help.
  --info            Display .NET information.
  --list-sdks       Display the installed SDKs.
  --list-runtimes   Display the installed runtimes.

path-to-application:
  The path to an application .dll file to execute."""

from docopt import docopt

def main(args):
    print(args)
if __name__ == '__main__':
    arguments = docopt(__doc__, version="0.0.1")
    print(arguments)
