class DecisionTree:
    def __init__(self, root, theme):
        self.__root = root
        self.__theme = theme


    @property
    def theme(self):
        return self.__theme
    
    @property
    def root(self):
        return self.__root