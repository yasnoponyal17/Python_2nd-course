def gen_bin_tree(height=6, root=2, left_branch=lambda r: r*3, right_branch=lambda r: r+4):
    if height <= 0:
        return {}
    
    tree = {"root": root}
    stack = [(root, 1, "root")]  # (value, level, path)
    
    while stack:
        value, level, path = stack.pop()
        
        if level >= height:
            continue
        
        left_val = left_branch(value)
        right_val = right_branch(value)
        
        left_key = f"left {path}"
        right_key = f"right {path}"
        
        tree[left_key] = left_val
        tree[right_key] = right_val
        
        stack.append((right_val, level + 1, right_key))
        stack.append((left_val, level + 1, left_key))
    
    return tree

# Пример использования
tree = gen_bin_tree()
print(tree)