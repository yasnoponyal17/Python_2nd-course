height = 6
root = 9

def gen_bin_tree(height, root):
    if height == 0:
        return None
    return {
        'root': root,
        'left': gen_bin_tree(height - 1, root * 2 + 1),
        'right': gen_bin_tree(height - 1, root * 2 - 1)
    }

def print_tree(tree, level=0):
    if not tree:
        return None
    
    print_tree(tree['right'], level + 1)
    
    print("   " * level + str(tree['root']))
    
    print_tree(tree['left'], level + 1)

print("Бинарное дерево:")
print_tree(gen_bin_tree(height, root))


        
    

