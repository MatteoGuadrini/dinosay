import unittest
import dinosay.dinosay
from argparse import ArgumentParser


class TestCommandLine(unittest.TestCase):
    def test_argparse(self):
        self.assertIsInstance(dinosay.dinosay.parse_arguments(), ArgumentParser)


if __name__ == '__main__':
    unittest.main()
