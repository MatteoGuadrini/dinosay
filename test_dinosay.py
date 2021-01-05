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


class TestCore(unittest.TestCase):
    def test_wrap_text(self):
        wrapped = ds.wrap_text("Hi I'm a carnivorous dinosaur who eats mostly curious men who do random tests! Oops!")
        self.assertEqual(len(wrapped), 84)

    def test_behavior_selector(self):
        normal = ds.behavior_selector('normal')
        self.assertEqual(normal.get('eye'), 'O O')
        normal = ds.behavior_selector('happy')
        self.assertEqual(normal.get('eye'), '^ ^')
        normal = ds.behavior_selector('cyborg')
        self.assertEqual(normal.get('eye'), '= =')

    def test_make_comic(self):
        comic = ds.make_comic("Hi dinosay!")
        self.assertEqual(comic, '/-------------\\\n| Hi dinosay! |\n\\-------------/')


if __name__ == '__main__':
    unittest.main()
