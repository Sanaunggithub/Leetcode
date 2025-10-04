def finalValueAfterOperations(self, operations):
        
    res = 0
    for o in operations:
        if o.startswith('++') or o.endswith('++'):
            res += 1

        elif o.startswith('--') or o.endswith('--'):
            res -= 1

    return res
