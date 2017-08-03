'''
Module containing class to render to console.
'''

from mazes.cell import Cell


class Render(object):
    '''
    Render to console.
    '''

    def __init__(self):
        '''
        Intialise.
        '''
        pass

    def render(self, grid):
        '''
        Render the passed grid.
        '''
        output = "+" + "---+" * grid.columns + "\n"
        for row in range(0, grid.rows):
            top = "|"
            bottom = "+"
            for col in range(0, grid.columns):
                cell = grid.lookup.get((row, col), Cell(-1, -1))
                body = "   "
                east_boundary = " " if cell.linked(cell.east) else "|"
                south_boundary = "   " if cell.linked(cell.south) else "---"
                corner = "+"
                top = top + body + east_boundary
                bottom = bottom + south_boundary + corner
            output = output + top + "\n"
            output = output + bottom + "\n"
        print(output)
