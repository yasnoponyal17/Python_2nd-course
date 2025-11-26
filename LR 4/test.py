import unittest
from tree import gen_bin_tree

class TestBinTree(unittest.TestCase):
  def test_example_1(self):
      tree = gen_bin_tree(height=0, root=9)
      self.assertEqual(tree, {'root': 9})

  def test_example_2(self):
      tree = gen_bin_tree(height=2, root=2)
      expectation = {
          'root': 2,
          'leftroot': 6,
          'rightroot': 6
      }
      self.assertEqual(tree, expectation)
      
  def test_example_3(self):
      tree = gen_bin_tree(height=3, root=3)
      expectation = {
          'root': 3,
          'leftroot': 9,
          'rightroot': 7,
          'leftleftroot': 27,
          'rightleftroot': 13,
          'leftrightroot': 21,
          'rightrightroot': 11
      }
      self.assertEqual(tree, expectation)
      
unittest.main(verbosity = 2)
						 
        