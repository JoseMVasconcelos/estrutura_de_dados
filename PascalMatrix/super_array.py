class SuperArray():
    def __init__(self, num1, num2):
        if num1 > num2:
            self.__min = num2
            self.__max = num1
        else:
            self.__min = num1
            self.__max = num2
        self.__array = [None]*(self.__max-self.__min+1)

    def atribui(self, pos, valor):
        pos_real = self.pega_pos_real(pos)
        self.__array[pos_real] = valor

    def acessa(self, pos):
        pos_real = self.pega_pos_real(pos)
        return self.__array[pos_real]

    def lista(self):
        return self.__array

    def pega_pos_real(self, pos):
        pos_real = pos - self.__min
        if (pos_real < 0) or (pos_real > self.__max - pos + 1):
            raise Exception("Fora dos limites!")
        else:
            return pos_real
