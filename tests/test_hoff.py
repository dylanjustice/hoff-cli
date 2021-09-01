from .context import hoff
import unittest

class HoffTest(unittest.TestCase):
    def when_hoff_called_given_no_arguments_then_returns_help(self):
        hoff.main()

    def when_hoff_called_given_version_arg_then_returns_version(self):
        hoff.main("-version")
    

if __name__ == '__main':
    unittest.main()