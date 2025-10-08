from collections import deque

height = int(input("Введите значение height: "))
root = int(input("Введите значение root: "))

def bin_tree(height, root):
    if height == 0:
        return None
    return {
        'root': root,
        'left': bin_tree(height - 1, root * 2 + 1),
        'right': bin_tree(height - 1, 2 * root - 1)
    }

def deque_tree(tree):
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

print("Значения дерева:", deque_tree(bin_tree(height, root)))