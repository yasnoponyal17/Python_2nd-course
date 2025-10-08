def bin_tree(height = 6, root = 2):
    if height == 0:
        return None
    
    dictionary_tree = {
        'root': root,
        'left': bin_tree(height - 1, root * 3),
        'right': bin_tree(height - 1, root + 4)
    }

    return dictionary_tree

def print_tree(tree, level=0):
    if not tree:
        return None
    
    print_tree(tree['right'], level + 1)
    print("   " * level + str(tree['root']))
    print_tree(tree['left'], level + 1)
