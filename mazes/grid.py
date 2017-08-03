'''
Module representing a grid of cells.
'''

from mazes.cell import Cell

import random


class Grid(object):
    '''
    Class representing a grid of cells.
    '''

    def __init__(self, rows, columns):
        '''
        Initialise.
        '''
        self.rows = rows
        self.columns = columns
        self.lookup = dict()
        self.prepare()
        self.configure()

    def prepare(self):
        '''
        Prepare the grid. Creates a cell for each coordinate.
        '''
        for row in range(self.rows):
            for col in range(self.columns):
                cell = Cell(row, col)
                self.lookup[cell.coords] = cell

    def configure(self):
        '''
        Configure the neighbour cells.
        '''
        for key, value in self.lookup.iteritems():
            row, col = key
            value.north = self.lookup.get((row - 1, col), None)
            value.south = self.lookup.get((row + 1, col), None)
            value.west = self.lookup.get((row, col - 1), None)
            value.east = self.lookup.get((row, col + 1), None)

    def size(self):
        '''
        Return rows * columns
        '''
        return self.rows * self.columns

    def random_cell(self):
        '''
        Return a random cell from the grid.
        '''
        random_row = random.randrange(0, self.rows)
        random_col = random.randrange(0, self.columns)
        return self.lookup.get((random_row, random_col))
