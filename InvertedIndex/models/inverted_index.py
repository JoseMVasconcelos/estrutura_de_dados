class InvertedIndex:
    def __init__(self):
        self.__directory = {}

    @property
    def directory(self):
        return self.__directory
    
    def add_ref(self, col, row_id):
        if col in self.__directory:
            self.__directory[col].add(row_id)
        else:
            self.__directory.update({col: {row_id}})

    def del_ref(self, row_id):
        for col in self.__directory:
            self.__directory.get(col).discard(row_id)
        self.update_directories()
    
    def update_directories(self):
        for ref in self.__directory:
            if len(self.__directory.get(ref)) == 0:
                self.__directory.pop(ref)
                break