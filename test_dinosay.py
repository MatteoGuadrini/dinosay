import unittest
import dinosay.dinosay as ds
from argparse import ArgumentParser


class TestCommandLine(unittest.TestCase):
    def test_argparse(self):
        self.assertIsInstance(ds.parse_arguments(), ArgumentParser)

    def test_dinosaur_all_option(self):
        option = ds.parse_arguments()
        args = option.parse_args(['-d', "trex", '-c', '-b', 'crazy', '-i', '-t',
                                  '-e', "@ @", '-w',  '40', "Rooooooaaaaarrr"])
        self.assertEqual(args.dinosaur, 'trex')
        self.assertEqual(args.color, True)
        self.assertEqual(args.behavior, 'crazy')
        self.assertEqual(args.idea, True)
        self.assertEqual(args.tongue, True)
        self.assertEqual(args.eye, '@ @')
        self.assertEqual(args.wrap, 40)


if __name__ == '__main__':
    unittest.main()