import unittest
import dinosay.dinosay as ds
from dinosay import __version__
from argparse import ArgumentParser

print("dinosay test version {0}".format(__version__))


class TestCommandLine(unittest.TestCase):
    def test_argparse(self):
        self.assertIsInstance(ds.parse_arguments(), ArgumentParser)

    def test_dinosaur_all_option(self):
        option = ds.parse_arguments()
        args = option.parse_args(['-d', "trex", '-c', 'red', '-b', 'crazy', '-i', '-t',
                                  '-e', "@ @", '-w', '40', "Rooooooaaaaarrr"])
        self.assertEqual(args.dinosaur, 'trex')
        self.assertEqual(args.color, 'red')
        self.assertEqual(args.behavior, 'crazy')
        self.assertEqual(args.idea, True)
        self.assertEqual(args.tongue, True)
        self.assertEqual(args.eye, '@ @')
        self.assertEqual(args.wrap, 40)

    def test_list(self):
        option = ds.parse_arguments()
        args = option.parse_args(['-l'])
        self.assertTrue(args.list)

    def test_random_dinosaur(self):
        option = ds.parse_arguments()
        args = option.parse_args(['-r'])
        self.assertTrue(args.random)

    def test_dinosaur_behavior(self):
        option = ds.parse_arguments()
        args = option.parse_args(['-d', 'trex', '-b', 'happy'])
        bh = ds.behavior_selector(args.behavior)
        self.assertIn('^ ^', bh['eye'])


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
        comic2 = ds.make_comic("Hi dinosay!", **ds.COMIC_TYPE.get('cartoon'))
        self.assertEqual(comic2, '0ooooooooooooo0\no Hi dinosay! o\nOoooooooooooooO')

    def test_dino_object(self):
        trex = ds.Dino(ds.DINO_TYPE['tyrannosaurus'])
        self.assertIsInstance(trex, ds.Dino)

    def test_dino_color(self):
        trex = ds.Dino(ds.DINO_TYPE['tyrannosaurus'], color='green')
        trex.apply_color()
        self.assertIn('\033[92m', trex.body)
        trex.reset_color()
        self.assertEqual(trex.body, trex.original)


if __name__ == '__main__':
    unittest.main()
