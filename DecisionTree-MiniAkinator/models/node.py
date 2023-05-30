class Node:
    def __init__(self, root, key):
        self.__root_node = root
        self.__key = key
        self.__left = None
        self.__right = None
        self.__height = 1