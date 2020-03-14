class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in tmp.split()] for tmp in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index - 1].copy()

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
