'''
Module for a cell in a grid of a maze.
'''


class Cell(object):
    '''
    A cell is essentially a col, row co-ordinate with some
    extra bits for linkage.
    '''

    def __init__(self, row, column):
        '''
        Initialise.
        '''
        self.coords = (row, column)
        self.links = set()
        self.north = None
        self.west = None
        self.south = None
        self.east = None

    def links(self):
        '''
        Return the links.
        '''
        return self.links

    def linked(self, cell):
        '''
        Return whether this cell has the supplied as a link.
        '''
        return cell in self.links

    def link(self, cell, bidirectional=True):
        '''
        Link this cell to the supplied. If bidirectional is True the link
        method on the passed instance will also be called with this instance.
        '''
        self.links.add(cell)
        if bidirectional and not cell.linked(self):
            cell.link(self, bidirection=False)

    def unlink(self, cell):
        '''
        Unlink the supplied cell from this cell. 
        '''
        if self.linked(cell):
            self.links.remove(cell)
        if cell.linked(self):
            cell.unlink(self)
