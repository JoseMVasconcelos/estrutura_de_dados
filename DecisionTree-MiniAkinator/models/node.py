class Node:
    def __init__(self, key, leaf):
        self.__key = key
        self.__isleaf = leaf
        self.__left = None
        self.__right = None

    @property
    def isleaf(self):
        return self.__isleaf
    
    @isleaf.setter
    def isleaf(self, isleaf):
        self.__isleaf = isleaf
    
    @property
    def key(self):
        return self.__key
    
    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, right):
        self.__right = right