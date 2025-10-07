import unittest

def bin_tree(height, root):
    if height == 0:
        return None
    
    dictionary_tree = {
        'root': root,
        'left': bin_tree(height - 1, root * 2 + 1),
        'right': bin_tree(height - 1, root * 2 - 1)
    }

    return dictionary_tree

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
        self.assertEqual(tree['left']['root'], 7)
        self.assertEqual(tree['right']['root'], 5)
        # 3 уровень дерева
        self.assertEqual(tree['left']['left']['root'], 15)
        self.assertEqual(tree['left']['right']['root'], 13)
        self.assertEqual(tree['right']['left']['root'], 11)
        self.assertEqual(tree['right']['right']['root'], 9)
        
				
unittest.main(verbosity = 2)