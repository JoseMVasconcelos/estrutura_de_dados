class Stack():
    def __init__(self, max):
        if isinstance(max, int) and max > 0:
            self.__max = max
        else:
            raise Exception("Invalid max value!")
        self.__stack = []
        self.__num_elements = 0

    @property
    def num_elements(self):
        return self.__num_elements
    
    def is_max(self):
        return (self.__num_elements == self.__max)

    def is_empty(self):
        return (self.__num_elements == 0)

    def push(self, data):
        if not self.is_max():
            self.__stack.append(data)
            self.__num_elements += 1
        else:
            raise Exception("Stack Overflow!")
    
    def pop(self):
        if not self.is_empty():
            self.__num_elements -= 1
            return self.__stack.pop()
        else:
            raise Exception("Empty Stack!")

    def top(self):
        if not self.is_empty():
            return self.__stack[self.__num_elements-1]
        else:
            raise Exception("Empty Stack!")
