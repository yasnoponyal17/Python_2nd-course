from collections import deque
from tree import bin_tree

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

print(deque_tree(bin_tree()))