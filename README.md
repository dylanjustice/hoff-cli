# hoff cli
<img src=https://ichef.bbci.co.uk/news/976/cpsprodpb/273D/production/_88554001_alamy_baywatch1_976.jpg />

## One part tribute to the [andculture](https://github.com/andculturecode) #hoff tradition
## One part tribute to the [and-cli](https://github.com/AndcultureCode/AndcultureCode.Cli) using python.

Command line tool to streamline common development and operations tasks

# Getting Started

The project is ready to run as is. You will need Python 2.7 or later.

## Create a Virtual Environment

After cloning or downloading the repo, create a Python virtual environment with:

```
python -m venv .virtualenv
```

for Python 3.x.

For Python 2.7, use the `virtualenv` command.

This will create the virtual environment in the project directory as `.virtualenv`. This is the convention I prefer as it keeps projects isolated from one another, but you can create your virtual environment whereever you like.

## Activate the Virtual Environment

Now activate the virtual environment. on macOS, Linux and Unix systems, use:

```
source .virtualenv/bin/activate
```

On Windows with `cmd.exe`:

```
.virtualenv\Scripts\activate.bat
```

Or Windows with PowerShell:

```
.\.virtualenv2\Scripts\activate.ps1
```

## Install the Development Environment

Now run:

```
pip install -e .[dev]
```

This will install the packages the project depends on in production as well as packages needed during development.

* The `-e` option specifies that you wish to install the package in "editable" mode for development.
* The `.[dev]` argument directs pip to install the package that is defined by the `setup.py` file the in the current directory and to additionally install the extra dependencies defined in the "dev" group. The additional dependencies include things lik ethe Sphinx documentation generator, pytest, pylint and other development packages that end-users of the package will not need.

Refer to the [pip install documentation](https://pip.pypa.io/en/stable/reference/pip_install/#) for more information on these options.

## Testing

You can run unit tests through setup.py with:

```
python setup.py test
```

or just run pytest directly:

```
pytest
```

## Documentation

To generate Sphinx documentation, run:

```
python setup.py build_sphinx
```

The generated documentation will be available in `build/sphinx`

## Distribution

When you are ready to distribute your Python package, build a wheel with:

```
python setup.py bdist_wheel
```

```
pip install --editable .
```

> Alternatively, you can add the `--universal` option to the `bdist_wheel` command to build a "univeral" distribution that can be used with both Python 3.x and 2.7.x.

The wheel will be generated in th `dist` directory.
