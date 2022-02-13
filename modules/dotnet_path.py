import glob
import os

cli_file_path_glob = "Presentation/Cli/bin/Debug/**/*Cli.dll"
data_project_file_paths_globs = [
    "*.csproj",
    "dotnet/*/Infrastructure/Data.SqlServer/Data.SqlServer.csproj",
    "dotnet/*/Infrastructure/Data.*/Data.*.csproj",
    "**/Data*.csproj",
    "**/*.csproj",
]
release_dir = "release"
solution_file_path_globs = [
    "*.sln",
    "dotnet/*.sln",
    "dotnet/*/*.sln",
    "**/*.sln"
]
web_project_file_path_globs = [
    "*.csproj",
    "dotnet/*/Presentation/Web/Web.csproj",
    "**/*Web.csproj",
    "**/*.csproj",
]


def solution_path():
    for pattern in solution_file_path_globs:
        files = glob.glob(pattern)
        if files:
            return files[0]
        continue
    return None


def solution_dir():
    path = solution_path()
    if path is None:
        return None

    return os.path.dirname(path)


def web_project_file_path():
    for pattern in web_project_file_path_globs:
        files = glob.glob(pattern)
        if files:
            return files[0]
        continue
    return None


def web_project_dir():
    path = web_project_file_path()
    if path is None:
        return None

    return os.path.dirname(path)
