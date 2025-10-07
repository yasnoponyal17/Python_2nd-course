from collections import deque

height = int(input("Введите значение height: "))
root = int(input("Введите значение root: "))

def gen_bin_tree(height, root):
    if height == 0:
        return None
    return {
        'root': root,
        'left': gen_bin_tree(height - 1, root * 2 + 1),
        'right': gen_bin_tree(height - 1, 2 * root - 1)
    }

def tree_deque(tree):
    if not tree:
        return None
    
    queue = deque([tree])
    result = []
    
    while queue:
        current = queue.popleft()
        if current:
            result.append(current['root'])
            queue.append(current.get('left'))
            queue.append(current.get('right'))
    
    return result

tree = gen_bin_tree(height, root)
print("Значения дерева:", tree_deque(tree))