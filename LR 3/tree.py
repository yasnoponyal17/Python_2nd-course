def gen_bin_tree(height = 2, root = 6, left_leaf = lambda x: x * 3, right_leaf = lambda x: x + 4):
    if height < 0:
        print('Высота дерева не может быть меньше нуля -_-')
        return None
    
    if height == 0:
        return {'root': root}
    

    if height > 0:
        dictionary_tree = {
            'root': root,
            'left': gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
            'right': gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)
        }
        return dictionary_tree

def print_tree(tree, level=0):
    if not tree:
        return None
    
    if 'right' in tree:
        print_tree(tree['right'], level + 1)

    print("   " * level + str(tree['root']))

    if 'left' in tree:
        print_tree(tree['left'], level + 1)

