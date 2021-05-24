class Matrix:
    def __init__(self, matrix_string):
        self.matrix_rows = [num for num in [row.split(' ') for row in matrix_string.split('\n')]]

    def row(self, index):
        row = self.matrix_rows[index - 1]
        num_row = [int(num) for num in row]
        return num_row

    def column(self, index):
        column = [int(row[index - 1]) for row in self.matrix_rows]
        return column