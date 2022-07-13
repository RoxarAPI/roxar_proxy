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

    def test_non_number(self):
        "Validate non number curve."
        log_run = roxar_proxy.LogRun()
        log_run.set_measured_depths([1, 2, 3, 4])
        curve = log_run.log_curves.create_discrete("DiscreteLog")
        with self.assertRaises(ValueError):
            curve.set_values([None, None, None, None])


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=1)
    sys.exit(not result.result.wasSuccessful())
