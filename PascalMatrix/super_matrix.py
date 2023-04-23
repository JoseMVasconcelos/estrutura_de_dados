class SuperMatrix():
    def __init__(self, num_lin, num_col):
        if isinstance(num_lin, int) and num_lin > 0:
            self.__num_lin = num_lin
        if isinstance(num_col, int) and num_col > 0:
            self.__num_col = num_col
        self.__super_matrix = [None]*self.__num_col*self.__num_lin

    def atribui(self, lin, col, valor):
        pos = pega_pos_real(lin, col)
        self.__super_matrix[pos] = valor

    def pega_pos_real(self, lin, col):
        pos = (lin*self.__num_lin) + col
        return pos