class Matrix(object):

    def __init__(self, matrix_string):
        self.table = []
        matrix_strings = matrix_string.split('\n')
        for x in matrix_strings:
          self.table.append(x.split(' '))

    def row(self, index):
        return [int(table_row) for table_row in self.table[index - 1]]

    def column(self, index):
        return [int(table_row[index - 1]) for table_row in self.table]
