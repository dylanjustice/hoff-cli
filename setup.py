from setuptools import setup

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup(
    name = "hoff-cli",
    author = "Dylan Justice",
    description = "Python port of the and-cli",
    version = "0.1.0",
    packages = "[hoff-cli]",
    install_requires = [req for req in requirements if req[:2] != "#"],
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'hoff = hoff-cli.hoff:main'
        ]
    }
)