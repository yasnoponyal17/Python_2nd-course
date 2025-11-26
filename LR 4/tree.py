from collections import deque

def gen_bin_tree(height=6, root=2, left=lambda l_r: l_r*3, right=lambda r_r: r_r+4):
    """
    Генерирует бинарное дерево в виде словаря.
    
    Аргументы:
        height: Высота дерева.
        root: Значение корневого узла.
        left: Функция для вычисления значения левого потомка.
        right: Функция для вычисления значения правого потомка.
    
    Возвращает:
        tree: Словарь, представляющий бинарное дерево. Ключ - путь к узлу, а значения - это значения узлов.
    """
    if height == 0:
        return {'root': root}
    
    tree = {'root': root}
    queue = deque([(root, 1, 'root')])
    
    while queue:
        value, lvl, path = queue.popleft()
        if lvl < height:
            left_value = left(value)
            right_value = right(value)
            tree[f'left{path}'] = left_value
            tree[f'right{path}'] = right_value
            queue.append((left_value, lvl+1, f'left{path}'))  
            queue.append((right_value, lvl+1, f'right{path}'))
    
    return tree


