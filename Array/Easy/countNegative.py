def countNegatives(grid):
        
    count = 0

    for g in grid:
        for gg in g:
            if gg < 0:
                count += 1


    return count