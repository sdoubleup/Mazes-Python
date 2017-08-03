'''
Module to perform a maze generation using BinaryTree algorithm.
'''

import random


def Generate(grid):
    '''
    Perform a BinaryTree maze generation on the grid.
    '''
    for row in range(0, grid.rows):
        for col in range(0, grid.columns):
            cell = grid.lookup.get((row, col), None)
            assert cell
            neighbours = [x for x in (cell.north, cell.east) if x is not None]
            neighbour = None if not neighbours else random.choice(neighbours)
            if neighbour:
                cell.link(cell=neighbour)
    return grid
