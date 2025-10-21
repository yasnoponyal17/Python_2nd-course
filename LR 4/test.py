import unittest
from tree import gen_bin_tree

class TestBinTree(unittest.TestCase):
  def test_example_1(self):
      tree = gen_bin_tree(height=0, root=9)
      self.assertEqual(tree, None)

  def test_example_2(self):
      tree = gen_bin_tree(height=2, root=2)
      self.assertEqual(tree['root'], 2)
      self.assertEqual(tree['leftroot'], 6)
      self.assertEqual(tree['rightroot'], 6)
      
  def test_example_3(self):
      tree = gen_bin_tree(height=3, root=3)
      # 1 уровень дерева
      self.assertEqual(tree['root'], 3) 
      # 2 уровень дерева
      self.assertEqual(tree['leftroot'], 9)    
      self.assertEqual(tree['rightroot'], 7)    
      # 3 уровень дерева 
      self.assertEqual(tree['leftleftroot'], 27) 
      self.assertEqual(tree['rightleftroot'], 13) 
      self.assertEqual(tree['leftrightroot'], 21)
      self.assertEqual(tree['rightrightroot'], 11) 
      
unittest.main(verbosity = 2)
						 
        