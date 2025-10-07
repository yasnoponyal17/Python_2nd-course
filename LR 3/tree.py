height = int(input("Введите значение height: "))
root = int(input("Введите значение root: "))

def bin_tree(height, root):
    if height == 0:
        return None
    
    dictionary_tree = {
        'root': root,
        'left': bin_tree(height - 1, root * 2 + 1),
        'right': bin_tree(height - 1, root * 2 - 1)
    }

    return dictionary_tree

def print_tree(tree, level=0):
    if not tree:
        return None
    
    print_tree(tree['right'], level + 1)
    
    print("   " * level + str(tree['root']))
    
    print_tree(tree['left'], level + 1)

print("Бинарное дерево:")
print_tree(bin_tree(height, root))
