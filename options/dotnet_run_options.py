from dataclasses import dataclass


@dataclass
class DotnetRunOptions:
    """Options for the dotnet run command"""
    build: bool
    clean: bool
    path: str
    restore: bool
    watch: bool