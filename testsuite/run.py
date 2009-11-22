#!/usr/bin/env python

import unittest
import sys

sys.path.append(".")

from sphinxtogithub.test import directoryhandler, filehandler, replacer


if __name__ == "__main__":

    suites = [
            filehandler.testSuite(),
            replacer.testSuite(),
            directoryhandler.testSuite(),
            ]

    suite = unittest.TestSuite(suites)
    
    runner = unittest.TextTestRunner()

    runner.run(suite)

