import unittest

from tree import bin_tree

class TestBinTree(unittest.TestCase):
    def test_example_1(self):
        tree = bin_tree(0, 9)
        self.assertEqual(tree, None)

    def test_example_2(self):
        tree = bin_tree(1, 9)
        self.assertEqual(tree['root'], 9)
        self.assertEqual(tree['left'], None)
        self.assertEqual(tree['right'], None)

    def test_example_3(self):
        tree = bin_tree(3, 3)
        # 1 уровень дерева
        self.assertEqual(tree['root'], 3) 
        # 2 уровень дерева
        self.assertEqual(tree['left']['root'], 9)
        self.assertEqual(tree['right']['root'], 7)
        # 3 уровень дерева
        self.assertEqual(tree['left']['left']['root'], 27)
        self.assertEqual(tree['left']['right']['root'], 13)
        self.assertEqual(tree['right']['left']['root'], 21)
        self.assertEqual(tree['right']['right']['root'], 11)
        
unittest.main(verbosity = 2)