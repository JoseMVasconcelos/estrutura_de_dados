class Node():
    def __init__(self, value, prev_node = None, next_node = None):
        self.__value = value
        self.__prev_node = prev_node
        self.__next_node = next_node

    @property
    def prev_node(self):
         return self.__prev_node    

    @prev_node.setter
    def prev_node(self, prev_node):
        self.__prev_node = prev_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node
    
    @property
    def value(self):
         return self.__value
    