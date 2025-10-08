from collections import deque

def bin_tree(height = 6, root = 2):
    if height == 0:
        return None
    return {
        'root': root,
        'left': bin_tree(height - 1, root * 3),
        'right': bin_tree(height - 1, root + 4)
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
