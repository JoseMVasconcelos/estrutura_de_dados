class InvertedIndex:
    def __init__(self, dir_name):
        self.__dir_name = dir_name
        self.__directory = {}

    @property
    def directory(self):
        return self.__directory
    
    def add_ref(self, col, row_id):
        if col in self.__directory:
            self.__directory[col].add(row_id)
        else:
            self.__directory.update({col: {row_id}})
        print(self.__directory)

    def del_ref(self, row_id):
        for col in self.__directory:
            self.__directory.get(col).discard(row_id)