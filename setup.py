from setuptools import setup

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup(
    name = "hoff-cli",
    author = "Dylan Justice",
    description = "Python port of the and-cli by Brandon Scott",
    version = "0.0.1",
    packages = "[hoff-cli]",
    install_requires = [req for req in requirements if req[:2] != "#"],
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'hoff = hoff-cli.hoff:main'
        ]
    }
)