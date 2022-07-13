"Roxar proxy unit tests."

import unittest
import sys

import roxar_proxy

class TestWellLog(unittest.TestCase):
    "Test well log API"

    def test_empty_md(self):
        "Validate empty MD curve"
        log_run = roxar_proxy.LogRun()
        with self.assertRaises(ValueError):
            log_run.set_measured_depths([])


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=1)
    sys.exit(not result.result.wasSuccessful())
