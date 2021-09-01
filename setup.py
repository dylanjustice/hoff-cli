from setuptools import find_packages, setup

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup(
    name = "hoff-cli",
    author = "Dylan Justice",
    description = "Python port of the and-cli",
    version = "0.1.0",
    packages = find_packages(exclude=('tests','docs')),
    install_requires = [req for req in requirements if req[:2] != "#"],
    include_package_data = True,
    entry_points = {
        'console_scripts': 
            ['hoff=hoff:main']
    }
)