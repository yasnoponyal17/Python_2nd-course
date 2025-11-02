def gen_bin_tree(height=6, root=2, left=lambda l_r: l_r*3, right=lambda r_r: r_r+4):
    if height == 0:
        return None
    
    tree = {'root': root}
    queue = [(root, 1, 'root')]
    
    while queue:
        value, lvl, path = queue.pop(0) 
        if lvl < height:
            left_value = left(value)
            right_value = right(value)
            tree[f'left{path}'] = left_value
            tree[f'right{path}'] = right_value
            queue.append((left_value, lvl+1, f'left{path}'))  
            queue.append((right_value, lvl+1, f'right{path}'))
    
    return tree


