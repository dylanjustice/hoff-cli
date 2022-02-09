import hoff.hoff

def test_when_hoff_called_given_no_arguments_then_returns_help():
    result = hoff.main()
    assert result

def test_when_hoff_called_given_version_arg_then_returns_version():
    result = hoff.main("-version")
    assert result

