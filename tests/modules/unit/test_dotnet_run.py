from models.options.dotnet_run_options import DotnetRunOptions
from modules.dotnet_run import DotnetRun, dotnet_run


def test_dotnet_run_when_path_is_none_then_returns_error_result():
    # Arrange

    # Act
    options = DotnetRunOptions(
        build=False, clean=False, path="", restore=False, watch=False)

    result = dotnet_run(options)

    # Assert
    assert result.status_code == 1
    assert result.message == DotnetRun.ERR_SLN_NOT_FOUND
