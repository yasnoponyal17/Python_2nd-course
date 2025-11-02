import unittest
from tree import gen_bin_tree

class TestBinTree(unittest.TestCase):
    def test_example_1(self):
        tree = gen_bin_tree(0, 9)
        self.assertEqual(tree['root'], 9)

    def test_example_2(self):
        tree = gen_bin_tree(1, 9)
        self.assertEqual(tree['root'], 9)
        self.assertIn('root', tree)
        self.assertIn('left', tree)
        self.assertIn('right', tree)
        
        
    def test_example_3(self):
        tree = gen_bin_tree(3, 3)
        self.assertEqual(tree['root'], 3) 
        self.assertIn('left', tree['left'])
        self.assertIn('left', tree['right'])
        self.assertIn('right', tree['left'])
        self.assertIn('right', tree['right'])
        self.assertIn('root', tree['left']['left'])
        self.assertIn('root', tree['left']['right'])
        self.assertIn('root', tree['right']['left'])
        self.assertIn('root', tree['right']['right'])
       
        
				
unittest.main(verbosity = 2)