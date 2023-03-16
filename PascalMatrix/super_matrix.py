class SuperMatrix():
    def __init__(self, num_lin, num_col):
        if isinstance(num_lin, int) and num_lin > 0:
            self.__num_lin = num_lin
        if isinstance(num_col, int) and num_col > 0:
            self.__num_col = num_col
        self.__super_matrix = [[0 for x in range(num_col)] for y in range(num_lin)]


